#strong password detection
import re

def is_strong_password(password):
    # Check if the password is at least eight characters long
    if len(password) < 8:
        return False

    # Check if the password contains both uppercase and lowercase characters
    if not re.search(r'[a-z]', password) or not re.search(r'[A-Z]', password):
        return False

    # Check if the password contains at least one digit
    if not re.search(r'\d', password):
        return False

    # If all checks pass, the password is strong
    return True

# Example usage:
password = input("Enter a password: ")
if is_strong_password(password):
    print("Password is strong.")
else:
    print("Password is not strong.")
