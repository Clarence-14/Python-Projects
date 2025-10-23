# A program that takes a user’s first and last name, manipulates the strings (e.g., uppercase, lowercase, length), and creates a formatted output.

first_name = input("Enter your first name:")
last_name = input("Enter your last name:")

full_name = f"{first_name}{last_name}"

uppercase_name = full_name.upper()
lowercase_name = full_name.lower()
name_length = len(full_name)

print(f"Full Name: {full_name}")
print(f"Uppercase: {uppercase_name}")
print(f"Lowercase: {lowercase_name}")
print(f"Length of Full Name: {name_length} characters")
