# A program that logs a user’s name and age to a text file, ensuring valid numeric input for age.

import datetime

def log_user_data():
    try:
        
        name = input("Enter your name: ")
        age_input = input("Enter your age: ")

        try:
            age = int(age_input)
        except ValueError:
            print("Invalid age input. Please enter a numeric value.")
            return  
    
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       
        try:
            with open("user_data.txt", "a") as file:
                file.write(f"Name: {name}, Age: {age}, Logged at: {timestamp}\n")
            print("User data logged successfully!")
        except IOError:
            print("Error writing to file. Please check file permissions.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the logger
log_user_data()

