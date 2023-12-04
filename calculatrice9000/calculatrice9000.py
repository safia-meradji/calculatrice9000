class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return num1 / num2

    def calculate(self, num1, num2, operator):
        if operator == "+":
            result = self.add(num1, num2)
        elif operator == "-":
            result = self.subtract(num1, num2)
        elif operator == "*":
            result = self.multiply(num1, num2)
        elif operator == "/":
            result = self.divide(num1, num2)
        else:
            raise ValueError("Invalid operator. Please use +, -, *, /")

        calculation = f"{num1} {operator} {num2} = {result}"
        self.history.append(calculation)
        return result, calculation

    def show_history(self):
        if not self.history:
            print("No calculations in the history.")
        else:
            for idx, calculation in enumerate(self.history, 1):
                print(f"{idx}. {calculation}")

    def clear_history(self):
        self.history = []
        print("History cleared.")


def get_user_input():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operator = input("Enter the operator (+, -, *, /): ")

            return num1, num2, operator
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

# Main program
calculator = Calculator()

while True:
    print("\nOptions:")
    print("1. Perform calculation")
    print("2. Show history")
    print("3. Clear history")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        num1, num2, operator = get_user_input()
        try:
            result, calculation = calculator.calculate(num1, num2, operator)
            print(f"Result: {result}")
            print(f"Calculation added to history: {calculation}")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == "2":
        calculator.show_history()
    elif choice == "3":
        calculator.clear_history()
    elif choice == "4":
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
