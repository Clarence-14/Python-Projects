# A program that converts a user-input list to a tuple and demonstrates tuple immutability by attempting to modify it.

def list_to_tuple(user_list):
    return tuple(user_list)

if __name__ == "__main__":
    user_input = input("Enter a list of items separated by spaces: ")
    user_list = user_input.split()
    
    result_tuple = list_to_tuple(user_list)
    print(f"Converted Tuple: {result_tuple}")
    
    try:
        result_tuple[0] = "modified"
    except TypeError as e:
        print(f"Error: {e} - Tuples are immutable and cannot be modified.")

        