# Simple Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator():
    print("===== Simple Calculator =====")
    print("Operations: +  -  *  /")
    print("Type 'quit' to exit")
    print("=============================\n")

    while True:
        # first number
        num1_input = input("Enter first number: ")
        if num1_input.lower() == 'quit':
            print("Goodbye!")
            break

        try:
            num1 = float(num1_input)
        except ValueError:
            print("Invalid number! Please try again.\n")
            continue

        # Get operator
        operator = input("Enter operator (+, -, *, /): ")
        if operator.lower() == 'quit':
            print("Goodbye!")
            break

        if operator not in ['+', '-', '*', '/']:
            print("Invalid operator! Please use +, -, *, /\n")
            continue

        # second number
        num2_input = input("Enter second number: ")
        if num2_input.lower() == 'quit':
            print("Goodbye!")
            break

        try:
            num2 = float(num2_input)
        except ValueError:
            print("Invalid number! Please try again.\n")
            continue

        # Calculate 
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)

        # Display result (remove .0 if it's a whole number)
        if isinstance(result, float) and result == int(result):
            result = int(result)

        print(f"\nResult: {num1} {operator} {num2} = {result}\n")
        print("-----------------------------\n")

# Run 
calculator()