Name = input("Enter your name: ")
print(f"Hello, {Name}! Welcome to the Expense Tracker App.")
expenses = []
budget = int(input("Enter your budget: "))


while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expenses")
    print("4. Show Highest Expense")
    print("5. Show Remaining Budget")
    print("6. Exit")


    choice = input("Enter your choice (1-6): ")

    if choice=='1':
        category = input("Enter expense category: ")
        amount = float(input("Enter expense amount: "))
        expenses.append((category, amount))
        print("Expense added successfully!")
    elif choice=='2':
        if not expenses:
            print("No expenses recorded")
        else:
            print("Expenses:")
            for index, (category, amount) in enumerate(expenses, start=1):
                print(f"{index}. {category}: ${amount:.2f}") 
    elif choice=='3':
        total_expenses = sum(amount for _, amount in expenses)
        print(f"Total expenses: ${total_expenses:.2f}")
    elif choice=='4':
        if not expenses:
            print("No expenses recorded")
        else:
            highest_expense = max(amount for _, amount in expenses)
            print(f"Highest expense: ${highest_expense:.2f}")
    elif choice=='5':
        total_expenses = sum(amount for _, amount in expenses)
        remaining_budget = budget - total_expenses
        print(f"Remaining budget: ${remaining_budget:.2f}")
        print(f"You have {'exceeded' if remaining_budget < 0 else 'remaining'} your budget by ${abs(remaining_budget):.2f}")
        
    elif choice=='6':
        print("Exiting the Expense Tracker App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
