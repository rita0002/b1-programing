# Exercise 3: Personal Expense Tracker

# 1. Initialize data structures
expense_records = []      # List to store all expenses
category_totals = {}      # Dictionary to store total per category
unique_categories = set() # Set to store unique categories

print("=== PERSONAL EXPENSE TRACKER ===\n")

# 2. Collect expense data
for i in range(1, 6):
    print(f"Enter expense {i}")

    category = input("Category: ")
    
    while True:
        try:
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("Please enter a valid number for amount.")

    date = input("Date (YYYY-MM-DD): ")

    # Store expense as a tuple
    expense_records.append((category, amount, date))
    print()

# 3. Categorize and sum expenses
for category, amount, date in expense_records:

    # Add category to set
    unique_categories.add(category)

    # Add amount to category total
    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount

# 4. Calculate overall statistics
amounts = []

for category, amount, date in expense_records:
    amounts.append(amount)

total_spending = sum(amounts)
average_expense = total_spending / len(amounts)
highest_expense = max(expense_records, key=lambda x: x[1])
lowest_expense = min(expense_records, key=lambda x: x[1])

# 5. Generate spending report
print("\n=== OVERALL SPENDING SUMMARY ===")
print(f"Total Spending: ${total_spending:.2f}")
print(f"Average Expense: ${average_expense:.2f}")
print(f"Highest Expense: ${highest_expense[1]:.2f} "
      f"(Category: {highest_expense[0]}, Date: {highest_expense[2]})")
print(f"Lowest Expense: ${lowest_expense[1]:.2f} "
      f"(Category: {lowest_expense[0]}, Date: {lowest_expense[2]})")

print("\n=== UNIQUE CATEGORIES SPENT ON ===")
print(unique_categories)
print(f"Total unique categories: {len(unique_categories)}")

print("\n=== SPENDING BY CATEGORY ===")
for category, total in category_totals.items():
    print(f"{category}: ${total:.2f}")

print("\n=== SPENDING CHART ===")
for category, total in category_totals.items():
    bars = int(total // 10)
    print(f"{category}: {'*' * bars}")

print("\n=== FILTER EXPENSES BY CATEGORY ===")
filter_category = input("Enter a category to filter (or press Enter to skip): ")

if filter_category:
    print(f"\nExpenses in category: {filter_category}")
    for category, amount, date in expense_records:
        if category.lower() == filter_category.lower():
            print(f"${amount:.2f} on {date}")

print("\nThank you for using my Personal Expense Tracker -By Rita!")
