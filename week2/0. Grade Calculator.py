# Grade Calculator

# Ask the user for their score
score = int(input("Enter your score (0-100): "))

# Determine grade using if-else
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

# Show the results
print("Your grade is:", grade)

# Bonus message for top grades
if grade == "A":
    print("Excellent work!")
if grade == "B":
    print("Good")
if grade == "C":
    print("Bad")
if grade == "D":
    print("Very Bad")
if grade == "F":
    print("Fail")
