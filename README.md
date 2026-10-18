# 💰 Expense Tracker — Flask Web Application

A web-based expense tracking application built with **Python and Flask** that allows users to register, log in, and manage their personal expenses securely.

The project demonstrates Flask web development, database integration, user authentication, password hashing, and user-specific data access.

## 🚀 Live Demo

**Live Application:** [Expense Tracker on Render](https://expense-tracker-flask.onrender.com/)

> Note: The first request may take some time because Render's free web services can spin down when inactive.

## ✨ Features

- **User Registration:** Create a new account with a username and password.
- **Secure Login:** Authenticate users using hashed passwords.
- **Session Management:** Manage authenticated sessions using Flask-Login.
- **Add Expenses:** Record expenses under the logged-in user's account.
- **View Expenses:** Display expenses belonging to the current user.
- **Delete Expenses:** Delete your own expenses securely.
- **User Data Isolation:** Prevent users from viewing or deleting other users' expenses through the application.
- **Protected Routes:** Require authentication to access protected pages.
- **Admin Support:** Support for administrator accounts through an `is_admin` field in the user model.
- **Cloud Deployment:** Deployed on Render and maintained using GitHub.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Flask-SQLAlchemy | Database integration |
| SQLite | Local and application database |
| Flask-Login | User authentication and sessions |
| Werkzeug Security | Password hashing and verification |
| HTML | Web page structure |
| Git & GitHub | Version control and source code management |
| Render | Cloud deployment |

## 🔐 Security Implementation

- Passwords are stored as hashes rather than plain text.
- Flask-Login manages authenticated user sessions.
- Protected routes require users to log in.
- Expense queries are filtered by the authenticated user's ID.
- Expense deletion checks ownership before deleting a record.
- The Flask secret key can be configured using an environment variable.
- Logout is handled through a POST request.

## ⚙️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/rishikesh-rajmane/expense-tracker-flask.git
cd expense-tracker-flask
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the secret key

Set a development secret key in PowerShell:

```powershell
$env:SECRET_KEY = "your-local-development-secret"
```

Use a strong, randomly generated secret key for any shared or production deployment. Keep secret values out of GitHub.

### 5. Start the application

```bash
python app.py
```

Open the local URL configured by the application in your browser.

## 🗄️ Database Information

The application uses SQLite through Flask-SQLAlchemy.

- The local database is stored separately from the GitHub repository.
- The database file is excluded from version control to avoid publishing personal expense records.
- On Render's free web service, local SQLite files use temporary storage and may be lost after restarts or redeployments.
- A persistent database solution is recommended before using the application for important real-world financial records.

## 📁 Project Structure

```text
expense-tracker-flask/
├── app.py
├── requirements.txt
├── .gitignore
└── templates/
    ├── index.html
    ├── login.html
    └── register.html
```

The SQLite database and local virtual environment are not included in the repository.

## 🎯 Learning Outcomes

Through this project, I have gained practical experience with:

- Building a web application using Flask.
- Connecting Python applications to a database.
- Implementing registration and login functionality.
- Hashing and verifying passwords.
- Managing user sessions and protected routes.
- Implementing user-specific data access.
- Using Git and GitHub for source control.
- Deploying a Flask application to Render.
- Managing application configuration through environment variables.

## 🔮 Future Improvements

- Integrate a persistent production database.
- Add expense categories and monthly summaries.
- Implement reporting and data visualization.
- Improve form validation and error handling.
- Add automated tests for authentication and expense access.

## 👨‍💻 Author

**Rishikesh Rajmane**

[GitHub Repository](https://github.com/rishikesh-rajmane/expense-tracker-flask)

---

*Built as a hands-on project to strengthen my Python, Flask, database, and backend development skills.*
