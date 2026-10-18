# Expense Tracker Web Application

A simple and user-friendly Expense Tracker built using **Python, Flask, SQLite, SQLAlchemy, HTML, and Tailwind CSS**. This project helps users record daily expenses, organize them by category, and monitor their spending through a web-based dashboard.

## Features

- **Add Expenses:** Enter an expense description, amount, date, and category.
- **View Expenses:** Display saved expense records in a table.
- **Delete Expenses:** Remove expense records when needed.
- **Expense Summary:** Calculate the total amount spent.
- **Category Management:** Organize expenses into categories such as Food, Transport, Rent, Utilities, and Health.
- **Date Filtering:** Filter expenses by a selected date range.
- **Responsive Dashboard:** A clean, dark-themed interface styled using Tailwind CSS.

*Note: Some dashboard features may still be under development.*

## Technologies Used

- **Python** — Application logic
- **Flask** — Web framework and routing
- **SQLite** — Database for storing expense records
- **Flask-SQLAlchemy** — Database operations and ORM
- **HTML5** — Web page structure
- **Tailwind CSS** — Dashboard styling
- **Git & GitHub** — Version control and project hosting

## Project Structure

```text
expense-tracker-static/
├── app.py
├── templates/
│   ├── index.html
│   ├── base.html
│   └── edit.html
├── instance/
│   └── expenses.db
├── venv/
└── .gitignore
```

The `instance/` and `venv/` folders are excluded from GitHub using `.gitignore`.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/expense-tracker-flask.git
cd expense-tracker-flask
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use the virtual environment's Python executable directly.

### 4. Install dependencies

```bash
pip install flask flask-sqlalchemy
```

### 5. Run the application

```bash
python app.py
```

### 6. Open the application

Visit the following address in your browser:

```text
http://127.0.0.1:4848
```

The SQLite database is created automatically when the application starts.

## Learning Objectives

This project was developed to gain practical experience with:

- Building web applications using Flask.
- Performing database operations with SQLite and SQLAlchemy.
- Handling and validating form submissions.
- Displaying database records dynamically using Jinja templates.
- Calculating totals from stored data.
- Using Git and GitHub to manage project versions.

## Future Improvements

- Complete and test date and category filtering.
- Add category-wise expense charts.
- Add monthly spending summaries.
- Implement CSV export.
- Add expense editing functionality.
- Deploy the application online.

## Author

Developed as a hands-on Python and database project to strengthen practical development skills.

