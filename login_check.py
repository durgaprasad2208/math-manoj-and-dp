import string

print("=== Strong Password Checker ===")

password = input("Enter your password: ")

# Conditions
has_upper = False
has_lower = False
has_number = False
has_symbol = False

# Check each character
for char in password:

    if char.isupper():
        has_upper = True

    elif char.islower():
        has_lower = True

    elif char.isdigit():
        has_number = True

    elif char in string.punctuation:
        has_symbol = True

# Check password length
if len(password) < 8:
    print("Weak Password!")
    print("Password should contain at least 8 characters.")

elif has_upper and has_lower and has_number and has_symbol:
    print("Strong Password!")

else:
    print("Weak Password!")

    if not has_upper:
        print("- Add at least one uppercase letter")

    if not has_lower:
        print("- Add at least one lowercase letter")

    if not has_number:
        print("- Add at least one number")

    if not has_symbol:
        print("- Add at least one special symbol")