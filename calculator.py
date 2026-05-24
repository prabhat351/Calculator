"""
calculator.py
A simple command-line calculator supporting basic arithmetic operations.
Includes addition, subtraction, multiplication, and division, with error handling.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b. Raises ValueError if division by zero."""
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed.")
    return a / b

def main():
    """
    Command-line interface for the calculator.
    Allows the user to perform basic arithmetic operations interactively.
    """
    print("Simple Python Calculator\n-------------------------")
    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Quit")
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in {'1', '2', '3', '4'}:
            print("Invalid input. Please select a valid operation.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        try:
            if choice == '1':
                result = add(num1, num2)
                op = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                op = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                op = '*'
            elif choice == '4':
                result = divide(num1, num2)
                op = '/'
            print(f"Result: {num1} {op} {num2} = {result}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
