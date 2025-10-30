# A function to calculate the factorial of a non-negative integer using recursion

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
if __name__ == "__main__":
    number = int(input("Enter a non-negative integer to calculate its factorial: "))
    try:
        result = factorial(number)
        print(f"The factorial of {number} is: {result}")
    except ValueError as e:
        print(e)

