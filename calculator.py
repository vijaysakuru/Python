import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Error: Cannot take the square root of a negative number"
    return math.sqrt(x)

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'power' for exponentiation")
    print("Enter 'sqrt' for square root")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide", "power", "sqrt"):
        if user_input == "sqrt":
            num = float(input("Enter a number: "))
            result = square_root(num)
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                result = add(num1, num2)
            elif user_input == "subtract":
                result = subtract(num1, num2)
            elif user_input == "multiply":
                result = multiply(num1, num2)
            elif user_input == "divide":
                result = divide(num1, num2)
            elif user_input == "power":
                result = power(num1, num2)

        print("Result: " + str(result))
    else:
        print("Unknown input. Please try again.")

