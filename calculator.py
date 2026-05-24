"""
calculator.py
Enhanced command-line calculator supporting arithmetic operations, calculation history, and memory functions.
"""
import math

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

def modulus(a, b):
    """Return the modulus (remainder) of a divided by b. Raises ValueError if modulus by zero.
    This function returns a result with the sign of the dividend (a), matching the C-style definition where:
        mod(a, b) = a - b * int(a / b)
    For example: modulus(-10, 3) == -1
    """
    if b == 0:
        raise ValueError("Error: Modulus by zero is not allowed.")
    # Use C-style modulus for integers
    if isinstance(a, int) and isinstance(b, int):
        return a - b * int(a / b)
    # For floats, fallback to Python behavior
    return a % b

def sqrt(x):
    """Return the square root of x. Raises ValueError if x is negative."""
    if x < 0:
        raise ValueError("Error: Square root of negative number is not allowed.")
    return math.sqrt(x)

# --- History and Memory Functions ---
def format_history_entry(entry):
    """Format a calculation history entry for display."""
    return entry

def print_history(history):
    """Display the calculation history list in a readable format."""
    if not history:
        print("No calculation history.")
    else:
        print("Calculation History:")
        for i, entry in enumerate(history, 1):
            print(f"{i}. {entry}")

def clear_history(history):
    """Clear the calculation history list."""
    history.clear()
    print("Calculation history cleared.")

def memory_store(memory, value):
    """Store value in memory (MS)."""
    memory['value'] = value
    print(f"Stored {value} in memory.")

def memory_recall(memory):
    """Recall value from memory (MR)."""
    if 'value' in memory:
        print(f"Memory Recall: {memory['value']}")
        return memory['value']
    else:
        print("No value stored in memory.")
        return None

def memory_clear(memory):
    """Clear memory value (MC)."""
    memory.clear()
    print("Memory cleared.")


def main():
    """
    Command-line interface for the calculator with history and memory functions.
    """
    print("Simple Python Calculator\n-------------------------")
    history = []
    memory = {}
    last_result = None
    while True:
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Square Root (√)")
        print("6. Modulus (%)")
        print("7. View History")
        print("8. Clear History")
        print("9. Memory Store (MS)")
        print("10. Memory Recall (MR)")
        print("11. Memory Clear (MC)")
        print("12. Quit")
        choice = input("Enter choice (1-12): ").strip()

        if choice == '12':
            print("Exiting calculator. Goodbye!")
            break

        if choice == '7':  # View History
            print_history(history)
            continue
        elif choice == '8':  # Clear History
            clear_history(history)
            continue
        elif choice == '9':  # Memory Store
            if last_result is not None:
                memory_store(memory, last_result)
            else:
                print("No result available to store in memory.")
            continue
        elif choice == '10':  # Memory Recall
            memory_recall(memory)
            continue
        elif choice == '11':  # Memory Clear
            memory_clear(memory)
            continue

        if choice not in {'1', '2', '3', '4', '5', '6'}:
            print("Invalid input. Please select a valid operation.")
            continue

        try:
            if choice == '5':
                num = float(input("Enter number: "))
                result = sqrt(num)
                entry = f"√{num} = {result}"
                print(f"Result: {entry}")
            elif choice == '6':
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                # Try to use int if possible for modulus
                if num1.is_integer() and num2.is_integer():
                    result = modulus(int(num1), int(num2))
                else:
                    result = modulus(num1, num2)
                entry = f"{num1} % {num2} = {result}"
                print(f"Result: {entry}")
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
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
                entry = f"{num1} {op} {num2} = {result}"
                print(f"Result: {entry}")
            history.append(entry)
            last_result = result
        except ValueError as e:
            print(e)
            last_result = None

if __name__ == "__main__":
    main()
