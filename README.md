# 💰 Expense Tracker — Flask Web Application

A web-based expense tracking application built using **Python and Flask** that allows users to register, log in, and manage their personal expenses securely.

The project demonstrates Flask web development, database integration, user authentication, password hashing, user-specific data access, and administrator-level user management.

## 🚀 Live Demo

**Live Application:** [Expense Tracker on Render](https://expense-tracker-flask-02a1.onrender.com/)

> Note: The first request may take some time because Render's free web services can spin down when inactive.

## ✨ Features

- **User Registration:** Create a new account with a username and password.
- **Secure Login:** Authenticate users using hashed passwords.
- **Session Management:** Manage authenticated sessions using Flask-Login.
- **Add Expenses:** Record expenses under the logged-in user's account.
- **View Expenses:** Display expenses belonging to the current user.
- **Delete Expenses:** Delete your own expenses securely.
- **Expense Filtering:** Filter expenses by date range and category.
- **Expense Summary:** Calculate total expenses based on selected filters.
- **Category-wise Analysis:** Visualize expenses by category.
- **Spending Visualization:** Display expense trends using charts.
- **User Data Isolation:** Prevent users from viewing or deleting other users' expenses through the application.
- **Protected Routes:** Require authentication to access protected pages.
- **Admin Dashboard:** Allow administrators to view and manage registered users.
- **User Management:** View usernames and account status.
- **Admin Password Reset:** Reset a user's password without accessing their original password.
- **Account Activation/Deactivation:** Administrators can activate or deactivate user accounts.
- **Role-based Access Control:** Restrict administrator features to authorized admin accounts.
- **Cloud Deployment:** Deployed on Render and maintained using GitHub.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Flask-SQLAlchemy | Database integration |
| SQLite | Local development database |
| PostgreSQL | Production database |
| Supabase | Hosted PostgreSQL database |
| Flask-Login | User authentication and sessions |
| Werkzeug Security | Password hashing and verification |
| SQLAlchemy | Database queries and ORM |
| HTML | Web page structure |
| Tailwind CSS | Frontend styling |
| Chart.js | Data visualization |
| Git & GitHub | Version control and source code management |
| Render | Cloud deployment |

## 🔐 Security Implementation

- Passwords are stored as secure hashes rather than plain text.
- Werkzeug Security handles password hashing and verification.
- Flask-Login manages authenticated user sessions.
- Protected routes require users to log in.
- Expense queries are filtered by the authenticated user's ID.
- Expense deletion checks ownership before deleting a record.
- Admin routes are protected using role-based access control.
- Only administrators can access user management functionality.
- Deactivated accounts cannot log in.
- Administrators can reset passwords without viewing original passwords.
- The Flask secret key and database connection are configured using environment variables.
- Logout is handled through a POST request.

## 👨‍💼 Admin User Management

The application includes an administrator-level user management feature.

Administrators can:

1. View all registered users.
2. Check user roles and account status.
3. Reset passwords for registered users.
4. Activate inactive accounts.
5. Deactivate user accounts.

Password security is maintained even during administrator password resets. The application stores only hashed passwords.

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

### 4. Configure environment variables

Set a development secret key in PowerShell:

```powershell
$env:SECRET_KEY = "your-local-development-secret"
```

For local development, the application uses SQLite by default.

To connect to Supabase PostgreSQL, configure:

```powershell
$env:DATABASE_URL = "YOUR_SUPABASE_DATABASE_CONNECTION_URL"
```

Keep database credentials and secret keys out of GitHub. Use URL encoding for special characters in database passwords.

### 5. Start the application

```bash
python app.py
```

Open the application:

```text
http://127.0.0.1:4848
```

## 🗄️ Database Information

The application uses Flask-SQLAlchemy to interact with its database.

- **Local Development:** SQLite database.
- **Production:** PostgreSQL database hosted on Supabase.
- **Database Configuration:** Managed through the `DATABASE_URL` environment variable.
- **User Table:** Stores usernames, password hashes, administrator roles, and account status.
- **Expense Table:** Stores expense descriptions, amounts, categories, dates, and associated user IDs.
- **Data Isolation:** Each user can access only their own expenses through the application.

The local SQLite database is excluded from GitHub using `.gitignore`.

The production database is hosted separately on Supabase, so application redeployments do not require storing the database inside the Render application filesystem.

## 📁 Project Structure

```text
expense-tracker-flask/
│
├── app.py
├── create_admin.py
├── requirements.txt
├── .gitignore
│
└── templates/
    ├── base.html
    ├── index.html
    ├── login.html
    ├── register.html
    ├── admin_users.html
    └── reset_password.html
```

The database file, virtual environment, and sensitive configuration values are not included in the repository.

## 🎯 Learning Outcomes

Through this project, I have gained practical experience with:

- Building a web application using Flask.
- Connecting Python applications to relational databases.
- Working with SQLite and PostgreSQL.
- Implementing registration and login functionality.
- Hashing and verifying passwords.
- Managing user sessions using Flask-Login.
- Implementing role-based access control.
- Developing administrator-level user management.
- Implementing user-specific data access.
- Writing database queries using SQLAlchemy.
- Creating expense summaries and visualizations.
- Using Git and GitHub for source control.
- Deploying a Flask application to Render.
- Managing application configuration through environment variables.

## 🔮 Future Improvements

- Add forgot-password functionality through email verification.
- Implement monthly and yearly expense reports.
- Add budget planning and spending alerts.
- Export expense reports to Excel and PDF.
- Improve dashboard responsiveness and user experience.
- Add automated tests for authentication and expense access.
- Enhance admin dashboard with user activity statistics.

## 👨‍💻 Author

**Rishikesh Rajmane**

[GitHub Repository](https://github.com/rishikesh-rajmane/expense-tracker-flask)

---

*Built as a hands-on project to strengthen my Python, Flask, database management, backend development, and application deployment skills.*
