# A program that asks the user to input two numbers and checks conditions using comparison and logical operators, outputting boolean results.

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

is_equal = (num1 == num2) 
is_greater = (num1 > num2)
is_less = (num1 < num2)

print(f"{num1}>{num2}: boolean: {is_greater}")
print(f"{num1}<{num2}: boolean: {is_less}")
print(f"{num1}={num2}: boolean: {is_equal}")
