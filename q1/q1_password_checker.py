import string

def check_password_strength(password: str) -> bool:
    """
    Returns True if password meets all rules, else False.

    Rules:
    - At least 8 characters
    - Contains lowercase
    - Contains uppercase
    - Contains at least one digit
    - Contains at least one special character
    """
    if len(password) < 8:
        return False

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_chars = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    has_special = any(c in special_chars for c in password)

    return has_lower and has_upper and has_digit and has_special


def get_feedback(password: str) -> list[str]:
    """Return a list of reasons why the password is weak (if any)."""
    reasons = []
    if len(password) < 8:
        reasons.append("❌ Minimum length should be 8 characters.")
    if not any(c.islower() for c in password):
        reasons.append("❌ It should contain at least one lowercase letter.")
    if not any(c.isupper() for c in password):
        reasons.append("❌ It should contain at least one uppercase letter.")
    if not any(c.isdigit() for c in password):
        reasons.append("❌ It should contain at least one digit (0-9).")
    if not any(c in string.punctuation for c in password):
        reasons.append("❌ It should contain at least one special character (e.g. !,@,#,$,%).")
    return reasons


if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")

    if check_password_strength(user_password):
        print("✅ Strong password! It meets all the criteria.")
    else:
        print("⚠️ Weak password. Please fix the following:")
        for reason in get_feedback(user_password):
            print(" -", reason)
