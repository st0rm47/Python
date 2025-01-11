###--->Making a Simple Calculator

def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b == 0:
        return "Division by Zero is not possible"
    return a/b

def calculator():
    while True:
        print("\nSimple Calculator")
        print("===================")
        print("Select an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        try:
            operand = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 5.")
            continue

        if operand == 5:
            print("Exiting the calculator. Goodbye!")
            break

        if operand not in [1, 2, 3, 4]:
            print("Invalid choice! Please select a valid operation.")
            continue

        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if operand == 1:
            print(f"{a} + {b} = {addition(a, b)}")
        elif operand == 2:
            print(f"{a} - {b} = {subtraction(a, b)}")
        elif operand == 3:
            print(f"{a} * {b} = {multiplication(a, b)}")
        elif operand == 4:
            result = division(a, b)
            print(f"{a} / {b} = {result}")

if __name__ == "__main__":
    calculator()