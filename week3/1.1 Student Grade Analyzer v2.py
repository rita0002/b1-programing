# Exercise 2: Student Grade Analyzer 
# This program stores student names and scores, calculates statistics, finds unique scores, and counts how many students got each score.

print("=== STUDENT GRADE ANALYZER ===\n")

# Step 1: Create empty data structures

student_records = []        # List to store (name and score)
stats = {}                  # Dictionary to store statistics


# Step 2: Collecting the students data

for i in range(1, 7):
    print(f"Enter details for Student {i}")
    
    name = input("Student name: ")
    score = int(input("Student score: "))
    
    # Store name and score as a tuple
    student_records.append((name, score))
    print()


# Step 3: Extract scores into a list

scores = []
for name, score in student_records:
    scores.append(score)


# Step 4: Calculate statistics

stats["highest"] = max(scores)
stats["lowest"] = min(scores)
stats["average"] = sum(scores) / len(scores)


# Step 5: Assign letter grades

letter_grades = {}   # Dictionary to store student name and letter grade

for name, score in student_records:
    if score >= 90:
        letter_grades[name] = "A"
    elif score >= 80:
        letter_grades[name] = "B"
    elif score >= 70:
        letter_grades[name] = "C"
    elif score >= 60:
        letter_grades[name] = "D"
    else:
        letter_grades[name] = "F"

# Step 6: Calculate median score

sorted_scores = sorted(scores)
middle = len(sorted_scores) // 2

if len(sorted_scores) % 2 == 0:
    median = (sorted_scores[middle - 1] + sorted_scores[middle]) / 2
else:
    median = sorted_scores[middle]


# Step 5: Find unique scores

unique_scores = set(scores)


# Step 6: Count grade distribution

grade_distribution = {}     # Dictionary to count scores
for score in scores:
    grade_distribution[score] = grade_distribution.get(score, 0) + 1


# Step 7: Display student results

print("\n" + "=" * 40)
print("=== STUDENT RECORDS ===")
print("=" * 40)

for i, (name, score) in enumerate(student_records, 1):
    print(f"{i}. {name}: {score}")

print("\n=== LETTER GRADES ===")
for name, grade in letter_grades.items():
    print(f"{name}: {grade}")


# Step 8: Display statistics

print("\n" + "=" * 40)
print("=== CLASS STATISTICS ===")
print("=" * 40)

print(f"Highest Score: {stats['highest']}")
print(f"Lowest Score: {stats['lowest']}")
print(f"Average Score: {stats['average']:.2f}")
print(f"Median Score: {median}")

# Step 8: Display Performance of students

print("\n=== PERFORMANCE ANALYSIS ===")

for name, score in student_records:
    if score >= stats["average"]:
        print(f"{name}: Above Average")
    else:
        print(f"{name}: Below Average")


# Step 9: Display unique scores

print("\n" + "=" * 40)
print("=== UNIQUE SCORES ===")
print("=" * 40)

print(unique_scores)
print(f"Total unique scores: {len(unique_scores)}")


# Step 10: Display grade distribution

print("\n" + "=" * 40)
print("=== GRADE DISTRIBUTION ===")
print("=" * 40)

for score in sorted(grade_distribution.keys(), reverse=True):
    count = grade_distribution[score]
    student_word = "student" if count == 1 else "students"
    print(f"Score {score}: {count} {student_word}")

import json 

# Prepare data to save
data_to_save = {
    "students": student_records,
    "statistics": stats,
    "unique_scores": list(unique_scores),
    "grade_distribution": grade_distribution,
    "letter_grades": letter_grades
}

# Save to JSON file
with open("student_results.json", "w") as file:
    json.dump(data_to_save, file, indent=4)

print("\nResults saved to student_results.json")
