# A module with utility functions (e.g., check if a number is prime, calculate its square) and use it in a main program.

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def square(n):
    """Calculate the square of a number."""
    return n * n
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
    print(f"The square of {number} is {square(number)}.")