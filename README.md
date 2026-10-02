# 🔐 Authentication System

A basic authentication system built using **Python, Flask, and SQLite**.

This project demonstrates common authentication practices such as secure password hashing, session-based authentication, input validation, protected routes, and basic protection against repeated failed login attempts.

## ✨ Features

- 👤 User registration
- 🔑 User login
- 🚪 User logout
- 🔒 Secure password hashing
- 🛡️ Session-based authentication
- 🔐 Protected dashboard
- ✅ Input validation
- 🚫 Duplicate username prevention
- ⏱️ Protection against repeated failed login attempts
- 🗄️ SQLite database
- 🎨 Simple web interface

## 🛠️ Technologies Used

- 🐍 Python
- 🌐 Flask
- 🗄️ SQLite
- 📄 HTML
- 🎨 CSS
- 🔐 Werkzeug Security

## 📁 Project Structure

    authentication-system/
    │
    ├── app.py
    ├── README.md
    ├── DECISIONS.md
    ├── SECURITY.md
    ├── requirements.txt
    ├── LICENSE
    ├── .gitignore
    │
    ├── templates/
    │   ├── login.html
    │   ├── register.html
    │   └── dashboard.html
    │
    └── static/
        └── style.css

## 🔄 Authentication Flow

    User Registration
           ↓
    Input Validation
           ↓
    Password Hashing
           ↓
    Store User in Database
           ↓
          Login
           ↓
    Verify Password Hash
           ↓
    Create Session
           ↓
    Protected Dashboard
           ↓
         Logout
           ↓
      Clear Session

## 📝 Registration

During registration, the user provides a username and password.

The application:

1. Validates the input.
2. Checks whether the username already exists.
3. Hashes the password using Werkzeug.
4. Stores the username and password hash in SQLite.

The original password is never stored as plain text.

## 🔑 Login

During login, the application:

1. Receives the username and password.
2. Finds the corresponding user in the database.
3. Verifies the entered password against the stored password hash.
4. Creates an authenticated session after successful verification.
5. Redirects the user to the dashboard.

## 🛡️ Session-Based Authentication

After successful login, the application creates a Flask session containing the authenticated user's information.

Protected routes check whether the user has an active session.

If the user is not authenticated, access to the protected dashboard is denied and the user is redirected to the login page.

## 🚪 Logout

When the user clicks logout, the application clears the authentication session.

The user must log in again to access the protected dashboard.

# 🔒 Security Measures

## 1. 🔐 Password Hashing

Passwords are not stored in plain text.

The application uses Werkzeug's password hashing functions:

    generate_password_hash()

to create password hashes and:

    check_password_hash()

to verify passwords during login.

This means that the database stores a password hash instead of the user's original password.

## 2. ✅ Input Validation

The application validates user input before processing it.

Validation includes:

- Required username
- Required password
- Username length
- Minimum password length
- Duplicate username checking

The password must contain at least 8 characters.

## 3. 🛡️ SQL Injection Protection

Database queries use parameterized SQL queries instead of directly inserting user input into SQL statements.

Example:

    connection.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    )

Using parameters helps prevent SQL injection through the username field.

## 4. 🔐 Protected Routes

The dashboard is an authenticated route.

Users who are not logged in cannot directly access the dashboard.

The application checks the session before displaying protected content.

## 5. ⏱️ Protection Against Repeated Failed Logins

The application tracks failed login attempts.

After 5 failed login attempts, further login attempts for that username are temporarily blocked for 60 seconds.

This provides basic protection against repeated password-guessing attempts.

The failed-attempt tracking is stored in memory, so this implementation is intended for an educational project rather than a production authentication system.

## 6. 👤 Unique Usernames

Usernames are stored with a unique database constraint.

This prevents multiple accounts from being created with the same username.

## 7. 🗄️ Local Database Protection

The SQLite database file is generated locally and is excluded from Git using .gitignore.

The database file is therefore not intended to be uploaded to the GitHub repository.

# ⚠️ Common Authentication Risks Addressed

| Security Risk | Protection Used |
|---|---|
| Plain-text password storage | Password hashing |
| SQL Injection | Parameterized SQL queries |
| Unauthorized dashboard access | Session-based authentication |
| Invalid input | Input validation |
| Repeated failed logins | Temporary login blocking |
| Duplicate usernames | Database unique constraint |
| Accidental database upload | .gitignore |

# 🚀 Installation

## 1. Clone the Repository

    git clone https://github.com/YOUR-USERNAME/authentication-system.git

Replace YOUR-USERNAME with your GitHub username.

## 2. Open the Project

    cd authentication-system

## 3. Install Dependencies

    pip install -r requirements.txt

## 4. Run the Application

    python app.py

## 5. 🌐 Open the Application

Open the following address in your browser:

    http://127.0.0.1:5000

The SQLite database will be created automatically when the application starts.

# 🗄️ Database

The project uses SQLite to store registered users.

The database contains:

    users
    ├── id
    ├── username
    └── password_hash

Passwords are stored as hashes rather than plain-text passwords.

The local database.db file is excluded from GitHub using .gitignore.

# ⚠️ Limitations

This project is designed as an educational demonstration of basic authentication security.

A production authentication system would require additional security measures, such as:

- HTTPS
- CSRF protection
- Persistent rate limiting
- Secure production session configuration
- Secure secret management
- Password reset functionality
- Email verification
- Account recovery
- Security logging and monitoring
- More advanced brute-force protection

# 🎯 Learning Objective

The objective of this project is to build a basic authentication system and demonstrate how common authentication risks can be reduced using standard security practices.

The project demonstrates:

- Secure password storage
- Authentication
- Authorization
- Session management
- Input validation
- SQL injection prevention
- Basic rate limiting
- Protected routes

# 📌 Project Status

**Version:** 1.0

The basic authentication functionality is implemented and working.

# 📄 License

This project is licensed under the MIT License.

See the `LICENSE` file for details.
