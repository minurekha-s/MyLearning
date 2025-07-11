# Login Page Project
# This script simulates a login page in the terminal.
# The username must be a valid email address.
# The password must be at least 8 characters, alphanumeric, and contain a special character.
# The user can only log in if both criteria are met.

import re

def is_valid_email(email):
    # Simple regex for email validation
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def is_valid_password(password):
    # At least 8 characters, contains letters, numbers, and special character
    if len(password) < 8:
        return False
    has_alpha = any(c.isalpha() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    return has_alpha and has_digit and has_special

def login_page():
    print("=== Login Page ===")
    email = input("Enter your email address: ").strip()
    if not is_valid_email(email):
        print("Error: Invalid email address.")
        return
    password = input("Enter your password: ").strip()
    if not is_valid_password(password):
        print("Error: Password must be at least 8 characters, alphanumeric, and contain a special character.")
        return
    print("Login successful! Welcome.")

if __name__ == "__main__":
    login_page()
