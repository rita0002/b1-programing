# Exercise 1: Failed Login Detector

# Step 1: Sample login attempts
login_attempts = [
    ("alice", "success"),
    ("bob", "failed"),
    ("bob", "failed"),
    ("charlie", "success"),
    ("bob", "failed"),
    ("alice", "failed")
]

# Step 2: Dictionary to track failed attempts
failed_count = {}

print("Checking login attempts...\n")

# Step 3: Loop through all login attempts
for username, status in login_attempts:
    if status == "failed":
        # Add 1 to user's failed count, or start with 1 if first failure
        failed_count[username] = failed_count.get(username, 0) + 1
        
        # Step 4: Alert if failures reach 3
        if failed_count[username] == 3:
            print(f"ALERT: User '{username}' has 3 failed login attempts!")

print("\nSecurity check complete.")
