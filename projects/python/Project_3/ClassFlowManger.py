class FinanceTracker:
    def __init__(self):
        self.income = 0
        self.expenses = 0

    def add_income(self, amount):
        if amount < 0:
            print("Income cannot be negative.")
        else:
            self.income += amount
            print(f"Income of ${amount} added.")

    def add_expense(self, amount):
        if amount < 0:
            print("Expense cannot be negative.")
        else:
            self.expenses += amount
            print(f"Expense of ${amount} added.")

    def get_balance(self):
        return self.income - self.expenses

    def show_summary(self):
        print("\n--- Finance Summary ---")
        print(f"Total Income: ${self.income}")
        print(f"Total Expenses: ${self.expenses}")
        print(f"Current Balance: ${self.get_balance()}")
        print("------------------------\n")

def main():
    tracker = FinanceTracker()
    while True:
        print("Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            tracker.add_income(amount)
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(amount)
        elif choice == '3':
            tracker.show_summary()
        elif choice == '4':
            print("Exiting Finance Tracker.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
