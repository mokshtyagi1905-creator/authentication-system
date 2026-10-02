# 🔐 Security Decisions

This file records important security decisions made during the development of the Authentication System.

## Decision 1: Password Storage

### ❌ Rejected Approach

Storing user passwords directly in the database as plain text.

### Why It Was Rejected

If the database were exposed, plain-text passwords could be directly read by anyone who gained access to the database.

This would create a serious security risk because users may also reuse passwords on other services.

### ✅ Revised Approach

Passwords are stored using secure password hashing with Werkzeug.

The application uses:

    generate_password_hash()

during registration and:

    check_password_hash()

during login.

This means the original password is not stored in the database.

## Decision 2: SQL Queries

### ❌ Rejected Approach

Building SQL queries by directly inserting user input into the SQL statement.

Example of the approach avoided:

    "SELECT * FROM users WHERE username = '" + username + "'"

### Why It Was Rejected

Directly inserting user input into SQL queries can allow SQL injection attacks.

### ✅ Revised Approach

Parameterized SQL queries are used instead.

Example:

    connection.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    )

This separates user input from the SQL command.

## Decision 3: Repeated Failed Login Attempts

### ❌ Rejected Approach

Allowing unlimited login attempts.

### Why It Was Rejected

Unlimited attempts make it easier to repeatedly guess passwords.

### ✅ Revised Approach

The application temporarily blocks login attempts for a username after 5 failed attempts.

The temporary block lasts for 60 seconds.

This provides basic protection against repeated failed login attempts.

## Summary

The main security decisions were made to reduce common authentication risks while keeping the project simple enough to understand and demonstrate.

The project prioritizes:

- 🔐 Secure password storage
- 🛡️ SQL injection prevention
- ⏱️ Basic login rate limiting
- 🔑 Session-based authentication
- ✅ Input validation
