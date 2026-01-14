import string
import random

# ---------------------------
# Part A: Individual Check Functions
# ---------------------------

def is_long_enough(pwd, minimum=8):
    """Return True if password meets the minimum length."""
    return len(pwd) >= minimum

def contains_upper(pwd):
    """Return True if password has at least one uppercase letter."""
    for c in pwd:
        if c.isupper():
            return True
    return False

def contains_lower(pwd):
    """Return True if password has at least one lowercase letter."""
    for c in pwd:
        if c.islower():
            return True
    return False

def contains_number(pwd):
    """Return True if password has at least one numeric digit."""
    return any(char.isdigit() for char in pwd)

def contains_special(pwd):
    """Return True if password has at least one special character."""
    specials = string.punctuation
    return any(char in specials for char in pwd)

# ---------------------------
# Part B: Master Validator
# ---------------------------

def password_validator(pwd):
    """Check all password rules and return a dictionary of results."""
    results = {
        "length_ok": is_long_enough(pwd),
        "has_upper": contains_upper(pwd),
        "has_lower": contains_lower(pwd),
        "has_digit": contains_number(pwd),
        "has_special": contains_special(pwd)
    }
    results["strong"] = all(results.values())
    return results

# ---------------------------
# Part C: User Interface
# ---------------------------

def main():
    print("="*50)
    print("PASSWORD VALIDATOR")
    print("="*50)
    print("\nPassword must meet the following rules:")
    print(" - Minimum 8 characters")
    print(" - At least one uppercase letter")
    print(" - At least one lowercase letter")
    print(" - At least one number")
    print(" - At least one special character (!@#$%^&* etc.)\n")
    
    password = input("Enter your password: ")
    
    results = password_validator(password)
    
    print("\n" + "="*50)
    print("CHECK RESULTS")
    print("="*50)
    
    symbol = {True: "✓", False: "✗"}
    print(f"{symbol[results['length_ok']]} Minimum length: {'Met' if results['length_ok'] else 'Not met'}")
    print(f"{symbol[results['has_upper']]} Contains uppercase: {'Met' if results['has_upper'] else 'Not met'}")
    print(f"{symbol[results['has_lower']]} Contains lowercase: {'Met' if results['has_lower'] else 'Not met'}")
    print(f"{symbol[results['has_digit']]} Contains number: {'Met' if results['has_digit'] else 'Not met'}")
    print(f"{symbol[results['has_special']]} Contains special char: {'Met' if results['has_special'] else 'Not met'}")
    
    print("\n" + "="*50)
    if results["strong"]:
        print("✓ PASSWORD IS STRONG!")
    else:
        print("✗ PASSWORD IS WEAK")
        # Suggest a random hint
        hints = []
        if not results["length_ok"]:
            hints.append(f"Add {8 - len(password)} more character(s)")
        if not results["has_upper"]:
            hints.append("Include at least one uppercase letter")
        if not results["has_lower"]:
            hints.append("Include at least one lowercase letter")
        if not results["has_digit"]:
            hints.append("Include a number")
        if not results["has_special"]:
            hints.append(f"Add a special character like {random.choice(string.punctuation)}")
        if hints:
            print("Hint: " + random.choice(hints))
    
    print("="*50)

if __name__ == "__main__":
    main()
