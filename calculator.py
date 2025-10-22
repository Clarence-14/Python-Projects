# This is a simple arithmetic calculator.

import math

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Perform basic arithmetic operations
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
    if num2 == 0:
        result = "Division by zero error"
else:
    result = "Invalid operator"


# Display the result
print("Result:", float(result))
