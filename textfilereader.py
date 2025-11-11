# A program that reads and displays the contents of a text file, handling cases where the file doesn’t exist.

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Error: The file does not exist."
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except IOError:
        return "Error: An I/O error occurred while reading the file."
    
if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    file_content = read_file(file_path)
    print(file_content)
