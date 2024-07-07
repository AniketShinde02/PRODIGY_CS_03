import re

def assess_password_strength(password):
    strength = 0

    # Length
    if len(password) >= 12:
        strength += 1

    # Uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1

    # Lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1

    # Numbers
    if re.search(r"\d", password):
        strength += 1

    # Special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength += 1

    if strength < 3:
        return "Weak"
    elif strength == 3 or strength == 4:
        return "Medium"
    else:
        return "Strong"

password = input("Enter a password: ")
strength = assess_password_strength(password)

print(f"Password strength: {strength}")
if strength == "Weak":
    print("Your password is weak. Consider adding more characters, uppercase letters, numbers, and special characters.")
elif strength == "Medium":
    print("Your password is medium strength. Consider adding more characters or special characters to make it stronger.")
else:
    print("Your password is strong! Good job!")