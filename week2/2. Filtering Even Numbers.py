# Python Program to Filter Even Numbers
# This program loops through a list of numbers and prints only the even ones.

# Step 1: Create a list of numbers
numbers = [12, 23, 34, 45, 56, 67, 78, 89, 90, 101]

# Step 2: Loop through each number in the pre-defined list
for number in numbers:
# Step 3: Check if the number is odd
    if number %2!= 0:
        # Skip this number because it's odd
        continue
    # Step 4: If the number is even, print it
    print(number)
