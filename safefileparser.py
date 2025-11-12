# A program that reads a text file containing numbers (one per line) and calculates their sum, skipping invalid lines.

def safe_file_parser(filename):
    valid_numbers = []
    invalid_count = 0

    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                try:
                    number = float(line)
                    valid_numbers.append(number)
                except ValueError:
                    print(f"Skipping invalid line: {line}")
                    invalid_count += 1

        # Calculate sum of valid numbers
        total_sum = sum(valid_numbers)

        # Print results
        print("Valid numbers:", valid_numbers)
        print("Sum of valid numbers:", total_sum)
        print("Count of valid lines:", len(valid_numbers))
        print("Count of invalid lines:", invalid_count)

        # Write valid numbers to a new file
        with open("valid_numbers.txt", "w") as outfile:
            for num in valid_numbers:
                outfile.write(str(num) + "\n")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print(f"Error: Could not read file '{filename}'.")
    finally:
        print("File parsing completed.")

safe_file_parser("numbers.txt")
