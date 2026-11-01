
from getpass import getpass

from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():

    username = input("Enter your existing username or email: ").strip()
    password = getpass("Enter your new admin password: ")
    confirm_password = getpass("Confirm your new password: ")

    if len(password) < 8:
        raise SystemExit("Password must be at least 8 characters.")

    if password != confirm_password:
        raise SystemExit("Passwords do not match.")

    existing_user = User.query.filter_by(username=username).first()

    if not existing_user:
        raise SystemExit("User not found.")

    existing_user.password_hash = generate_password_hash(password)
    existing_user.is_admin = True

    db.session.commit()

    print("Admin account updated successfully!")
