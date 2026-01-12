# Exercise 2: Student Grade Analyzer v1.0
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


# Step 8: Display statistics

print("\n" + "=" * 40)
print("=== CLASS STATISTICS ===")
print("=" * 40)

print(f"Highest Score: {stats['highest']}")
print(f"Lowest Score: {stats['lowest']}")
print(f"Average Score: {stats['average']:.2f}")


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

