from getpass import getpass
from app import app, db, User
from werkzeug.security import generate_password_hash

with app.app_context():

    username = input("Enter admin username or email: ").strip()
    password = getpass("Create admin password: ")
    confirm_password = getpass("Confirm admin password: ")

    if len(username) < 3:
        raise SystemExit("Username must be at least 3 characters.")

    if len(password) < 8:
        raise SystemExit("Password must be at least 8 characters.")

    if password != confirm_password:
        raise SystemExit("Passwords do not match.")

    user = User.query.filter_by(username=username).first()

    if user:
        user.password_hash = generate_password_hash(password)
        user.is_admin = True
        print("Existing user updated as admin!")
    else:
        user = User(
            username=username,
            password_hash=generate_password_hash(password),
            is_admin=True
        )
        db.session.add(user)
        print("New admin account created!")

    db.session.commit()

    print("Admin setup completed successfully!")