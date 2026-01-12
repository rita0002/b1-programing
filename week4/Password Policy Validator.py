# Exercise 3: Password Policy Validator
# This program checks if passwords meet basic security rules

# Step 1: List of passwords to check
passwords = ["Pass123", "SecurePassword1", "weak", "MyP@ssw0rd", "NOLOWER123"]

# Counters for summary
compliant_count = 0
non_compliant_count = 0

print("Validating passwords...\n")

# Step 2: Check each password
for pwd in passwords:
    issues = []  # List to store issues for this password

    # Check minimum length (8 characters)
    if len(pwd) < 8:
        issues.append("Too short")

    # Check for at least one uppercase letter
    if not any(char.isupper() for char in pwd):
        issues.append("No uppercase")

    # Check for at least one lowercase letter
    if not any(char.islower() for char in pwd):
        issues.append("No lowercase")

    # Check for at least one digit
    if not any(char.isdigit() for char in pwd):
        issues.append("No digits")

    # Step 3: Print result for this password
    if not issues:
        print(f"PASS: '{pwd}' - Meets all requirements")
        compliant_count += 1
    else:
        print(f"FAIL: '{pwd}' - {', '.join(issues)}")
        non_compliant_count += 1

# Step 4: Print summary
print(f"\nSummary: {compliant_count} compliant, {non_compliant_count} non-compliant")
