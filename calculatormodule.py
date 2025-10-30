# A simple calculator with separate functions for addition, subtraction, multiplication, and division.

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    if num1 == 0:
     raise ValueError("Multiplication by zero is not allowed.")
    elif num2 == 0:
     raise ValueError("Multiplication by zero is not allowed.")
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2

if __name__ == "__main__":
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        try:
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        except ValueError as e:
            print(e)
    elif choice == '4':
        try:
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid input")