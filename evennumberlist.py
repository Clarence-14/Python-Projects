# A program that takes a space-separated list of numbers and uses a list comprehension to filter even numbers.

def get_even_numbers(number_list):
    even_numbers = [num for num in number_list if num % 2 == 0]
    return even_numbers

if __name__ == "__main__":
    input_numbers = input("Enter a space-separated list of numbers: ")
    number_list = list(map(int, input_numbers.split()))
    even_numbers = get_even_numbers(number_list)
    print("Even numbers:", even_numbers)
    