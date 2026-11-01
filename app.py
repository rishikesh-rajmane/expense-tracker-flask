
from flask import (
    Flask, render_template, request, url_for,
    flash, redirect, abort
)
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager, UserMixin, login_user,
    logout_user, login_required, current_user
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date, datetime
from sqlalchemy import func
from functools import wraps
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL",
    "sqlite:///expenses.db"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = os.environ.get(
    "SECRET_KEY",
    "dev-only-change-this-local-key"
)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# ---------------- MODELS ----------------

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id'),
        nullable=True
    )


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


with app.app_context():
    db.create_all()


CATEGORIES = ['Food', 'Transport', 'Rent', 'Utilities', 'Health']


# ---------------- ADMIN ACCESS ----------------

def admin_required(view):
    @wraps(view)
    @login_required
    def wrapped_view(*args, **kwargs):
        if not current_user.is_admin:
            abort(403)
        return view(*args, **kwargs)

    return wrapped_view


# ---------------- REGISTER ----------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for("index"))

    if request.method == "POST":

        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""

        if not username or not password:
            flash("Username and password are required.", "error")
            return redirect(url_for("register"))

        if len(username) < 3:
            flash("Username must be at least 3 characters.", "error")
            return redirect(url_for("register"))

        if len(password) < 8:
            flash("Password must be at least 8 characters.", "error")
            return redirect(url_for("register"))

        if User.query.filter_by(username=username).first():
            flash("That username is already taken.", "error")
            return redirect(url_for("register"))

        user = User(
            username=username,
            password_hash=generate_password_hash(password),
            is_active=True
        )

        db.session.add(user)
        db.session.commit()

        login_user(user)

        flash("Account created successfully!", "success")
        return redirect(url_for("index"))

    return render_template("register.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect(url_for("index"))

    if request.method == "POST":

        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""

        user = User.query.filter_by(username=username).first()

        if (
            user
            and user.is_active
            and check_password_hash(user.password_hash, password)
        ):
            login_user(user)
            return redirect(url_for("index"))

        flash("Invalid username or password.", "error")
        return redirect(url_for("login"))

    return render_template("login.html")


# ---------------- LOGOUT ----------------

@app.route("/logout", methods=["POST"])
@login_required
def logout():

    logout_user()
    return redirect(url_for("login"))


# ---------------- ADMIN: VIEW USERS ----------------

@app.route("/admin/users")
@admin_required
def admin_users():

    users = User.query.order_by(User.id.desc()).all()

    return render_template(
        "admin_users.html",
        users=users
    )


# ---------------- ADMIN: RESET PASSWORD ----------------

@app.route("/admin/reset-password/<int:user_id>", methods=["GET", "POST"])
@admin_required
def reset_user_password(user_id):

    user = User.query.get_or_404(user_id)

    if request.method == "POST":

        password = request.form.get("password") or ""
        confirm_password = request.form.get("confirm_password") or ""

        if len(password) < 8:
            flash("Password must be at least 8 characters.", "error")
            return redirect(
                url_for("reset_user_password", user_id=user.id)
            )

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(
                url_for("reset_user_password", user_id=user.id)
            )

        user.password_hash = generate_password_hash(password)
        db.session.commit()

        flash("User password reset successfully.", "success")
        return redirect(url_for("admin_users"))

    return render_template(
        "reset_password.html",
        user=user
    )


# ---------------- ADMIN: ACTIVATE / DEACTIVATE ----------------

@app.route("/admin/toggle-user/<int:user_id>", methods=["POST"])
@admin_required
def toggle_user(user_id):

    user = User.query.get_or_404(user_id)

    if user.id == current_user.id:
        flash("You cannot deactivate your own admin account.", "error")
        return redirect(url_for("admin_users"))

    user.is_active = not user.is_active
    db.session.commit()

    if user.is_active:
        flash("User account activated.", "success")
    else:
        flash("User account deactivated.", "success")

    return redirect(url_for("admin_users"))


# ---------------- DATE FILTER ----------------

def parse_date_or_none(s: str):

    if not s:
        return None

    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return None


# ---------------- DASHBOARD ----------------

@app.route("/")
@login_required
def index():

    start_str = (request.args.get("start") or "").strip()
    end_str = (request.args.get("end") or "").strip()
    selected_category = (request.args.get("category") or "").strip()

    start_date = parse_date_or_none(start_str)
    end_date = parse_date_or_none(end_str)

    if start_date and end_date and end_date < start_date:
        flash("End date cannot be before start date.", "error")
        start_date = end_date = None
        start_str = end_str = ""

    q = Expense.query.filter_by(user_id=current_user.id)

    if start_date:
        q = q.filter(Expense.date >= start_date)

    if end_date:
        q = q.filter(Expense.date <= end_date)

    if selected_category:
        q = q.filter(Expense.category == selected_category)

    expenses = q.order_by(
        Expense.date.desc(),
        Expense.id.desc()
    ).all()

    total = round(sum(e.amount for e in expenses), 2)

    cat_q = db.session.query(
        Expense.category,
        func.sum(Expense.amount)
    ).filter(Expense.user_id == current_user.id)

    if start_date:
        cat_q = cat_q.filter(Expense.date >= start_date)

    if end_date:
        cat_q = cat_q.filter(Expense.date <= end_date)

    if selected_category:
        cat_q = cat_q.filter(Expense.category == selected_category)

    cat_rows = cat_q.group_by(Expense.category).all()

    cat_labels = [c for c, _ in cat_rows]
    cat_values = [round(float(s or 0), 2) for _, s in cat_rows]

    return render_template(
        "index.html",
        expenses=expenses,
        categories=CATEGORIES,
        today=date.today().isoformat(),
        total=total,
        start_str=start_str,
        end_str=end_str,
        selected_category=selected_category,
        cat_labels=cat_labels,
        cat_values=cat_values
    )


# ---------------- ADD EXPENSE ----------------

@app.route("/add", methods=["POST"])
@login_required
def add():

    description = (request.form.get("description") or "").strip()
    amount_str = (request.form.get("amount") or "").strip()
    category = (request.form.get("category") or "").strip()
    date_str = (request.form.get("date") or "").strip()

    if not description or not amount_str or not category:
        flash("Please fill description, amount, category.", "error")
        return redirect(url_for("index"))

    if category not in CATEGORIES:
        flash("Please select a valid category.", "error")
        return redirect(url_for("index"))

    try:
        amount = float(amount_str)

        if amount <= 0:
            raise ValueError

    except ValueError:
        flash("Amount must be a positive number.", "error")
        return redirect(url_for("index"))

    try:
        d = (
            datetime.strptime(date_str, "%Y-%m-%d").date()
            if date_str else date.today()
        )
    except ValueError:
        d = date.today()

    expense = Expense(
        description=description,
        amount=amount,
        category=category,
        date=d,
        user_id=current_user.id
    )

    db.session.add(expense)
    db.session.commit()

    flash("Expense added.", "success")
    return redirect(url_for("index"))


# ---------------- DELETE EXPENSE ----------------

@app.route("/delete/<int:expense_id>", methods=["POST"])
@login_required
def delete(expense_id):

    expense = Expense.query.filter_by(
        id=expense_id,
        user_id=current_user.id
    ).first_or_404()

    db.session.delete(expense)
    db.session.commit()

    flash("Expense deleted successfully.", "success")
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=4848)
