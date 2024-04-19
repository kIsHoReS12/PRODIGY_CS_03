import re
import getpass

def check_password_strength():
    password = getpass.getpass(prompt="Enter password to evaluate strength:")
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[ !@#$%&'()*+,-./\[\\\]^_`{|}~]", password) is None
    strength = 5
    errors = []
    if length_error:
        strength -= 1
        errors.append("Password length should be at least 8 characters.")
    if digit_error:
        strength -= 1
        errors.append("Password should contain at least one digit.")
    if uppercase_error:
        strength -= 1
        errors.append("Password should contain at least one uppercase letter.")
    if lowercase_error:
        strength -= 1
        errors.append("Password should contain at least one lowercase letter.")
    if special_char_error:
        strength -= 1
        errors.append("Password should contain at least one special character.")
    return strength, errors

def main():
    strength, errors = check_password_strength()
    if strength == 5:
        print("Your password is strong!")
    else:
        print("Your password is weak. Please consider the following:")
        for error in errors:
            print(" -", error)
    return strength

if __name__ == "__main__":
    passwordstr=0
    passwordstr=main()
    while(passwordstr!=5):
        passwordstr=main()
