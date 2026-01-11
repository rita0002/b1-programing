# Simple Login System with 3 Attempts
# This program asks the user for a password and allows only 3 attempts.
# If the user fails 3 times, access is locked.

#Set the correct password
correct_password = "ritarizz"

#Initialize attempt counter
attempts = 0

#Set maximum allowed attempts
max_attempts = 3

#Flag to track successful login
login_successful = False

#Start a loop for login attempts
while attempts < max_attempts:
    print(f"\n Attempt {attempts + 1} of {max_attempts}")
    
    # Ask user to enter password
    entered_password = input("Enter your password: ")
    
    # Check if entered password is correct
    if entered_password == correct_password:
        print("Password accepted! Welcome Back.")
        login_successful = True
        break  # Exit the loop if password is correct
    else:
        print("Incorrect password.")
        attempts += 1  # Increase attempt counter

#If login was not successful after all attempts
if not login_successful:
    print("Too many incorrect attempts. Access locked.")