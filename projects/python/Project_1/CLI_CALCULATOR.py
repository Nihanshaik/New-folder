import operator
import os

class CLICalculator:
    def __init__(self):
        self.history = []

    def display_menu(self):
        print("\nWelcome to the CLI Calculator!")
        print("Select an option:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. View History")
        print("6. Clear History")
        print("7. Exit")

    def get_operation(self, choice):
        operations = {
            '1': operator.add,
            '2': operator.sub,
            '3': operator.mul,
            '4': operator.truediv
        }
        return operations.get(choice, None)

    def perform_calculation(self, choice, num1, num2):
        operation = self.get_operation(choice)
        if operation:
            try:
                result = operation(num1, num2)
                expression = f"{num1} {choice} {num2} = {result}"
                self.history.append(expression)
                print("Result:", result)
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid operation choice. Please try again.")

    def view_history(self):
        if self.history:
            print("\nCalculation History:")
            for entry in self.history:
                print(entry)
        else:
            print("\nNo history available.")

    def clear_history(self):
        self.history.clear()
        print("History cleared successfully.")

    def start(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice in ['1', '2', '3', '4']:
                try:
                    num1 = float(input("Enter the first number: "))
                    num2 = float(input("Enter the second number: "))
                    self.perform_calculation(choice, num1, num2)
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
            elif choice == '5':
                self.view_history()
            elif choice == '6':
                self.clear_history()
            elif choice == '7':
                print("Thank you for using the CLI Calculator. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator = CLICalculator()
    calculator.start()
