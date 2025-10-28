# A program that calculates the sum of even numbers up to a user-specified limit using a while loop.

limit = int(input("Enter a positive integer limit: "))
sum_of_evens = 0
current_number = 2
while current_number <= limit:
    sum_of_evens += current_number
    current_number += 2
print(f"The sum of even numbers up to {limit} is: {sum_of_evens}")
