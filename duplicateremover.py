# A program that takes a list of numbers from the user and uses a set to remove duplicates.

def remove_duplicates(numbers):
    return list(set(numbers))

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    number_list = [int(num) for num in user_input.split()]
    
    unique_numbers = remove_duplicates(number_list)
    
    print(f"Original List: {number_list}")
    print(f"List after removing duplicates: {unique_numbers}")

    