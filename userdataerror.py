# A program that logs a user’s name and age to a text file, ensuring valid numeric input for age.

def log_user_data(name, age):
    try:
        age = int(age)
    except ValueError:
        return "Error: Age must be a number."
    
    with open("user_data.txt", "a") as file:
        file.write(f"Name: {name}, Age: {age}\n")
    
    return "User data logged successfully."

    try:
        age = int(age)
    except IOError:
        return "Error: An I/O error occurred while writing to the file."
    
    with open("user_data.txt", "a") as file:
        file.write(f"Name: {name}, Age: {age}\n")

if __name__ == "__main__":
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    
    result = log_user_data(name, age)
    print(result)

