# 🔒 Security Documentation

## Overview

This project is a basic authentication system created for educational purposes.

It demonstrates several common security practices used to protect authentication systems from common risks.

## 🔐 Password Security

User passwords are never stored as plain text.

During registration, passwords are converted into secure password hashes using Werkzeug's password hashing functions.

The application uses:

    generate_password_hash()

to create the password hash and:

    check_password_hash()

to verify passwords during login.

Only the password hash is stored in the SQLite database.

## 🛡️ SQL Injection Protection

The application uses parameterized SQL queries when communicating with the SQLite database.

For example:

    connection.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    )

User input is passed as a parameter instead of being directly inserted into the SQL statement.

This helps protect the application against SQL injection attacks.

## ✅ Input Validation

The application validates user input before processing it.

The following checks are performed:

- Username is required.
- Password is required.
- Username length is validated.
- Password must contain at least 8 characters.
- Duplicate usernames are rejected.

## 🔑 Session Authentication

The application uses Flask sessions to maintain authentication state.

After successful login, the user's session is created.

Protected routes check whether an authenticated session exists before allowing access.

Users who are not authenticated are redirected to the login page.

## 🚪 Logout

When a user logs out, the authentication session is cleared.

This prevents the previous authenticated session from being used to access the protected dashboard.

## ⏱️ Failed Login Protection

The application tracks failed login attempts.

After 5 failed login attempts for a username, login attempts are temporarily blocked for 60 seconds.

This provides basic protection against repeated password-guessing attempts.

The current implementation stores this information in memory, so it is intended for educational use rather than production deployment.

## 🗄️ Database Protection

The project uses SQLite to store user information.

The database stores:

- User ID
- Username
- Password hash

The local `database.db` file is excluded from Git using `.gitignore`.

This prevents local user data from being accidentally uploaded to the repository.

## 🔑 Secret Key

The Flask application requires a secret key for session security.

A real production deployment should store the secret key securely using an environment variable or secret-management system rather than hard-coding a real secret in the source code.

## ⚠️ Production Security Considerations

This project is an educational authentication demonstration and should not be considered production-ready.

A production application should additionally implement:

- HTTPS
- CSRF protection
- Secure cookie configuration
- Persistent rate limiting
- Stronger brute-force protection
- Secure secret management
- Password reset functionality
- Email verification
- Account recovery
- Security logging and monitoring
- Regular dependency updates
- Proper production server configuration

## 🎯 Security Objective

The security objective of this project is to demonstrate how common authentication risks can be reduced through:

- 🔐 Password hashing
- 🛡️ Parameterized database queries
- ✅ Input validation
- 🔑 Session-based authentication
- ⏱️ Failed-login protection
- 🗄️ Database and secret protection

These measures provide a basic foundation for understanding secure authentication design.
