# A program that stores 2D coordinates as tuples in a list and calculates the average x and y coordinates.

def calculate_average_coordinates(coordinates):
    if not coordinates:
        return (0, 0)
    
    total_x = 0
    total_y = 0
    count = len(coordinates)
    
    for coord in coordinates:
        total_x += coord[0]
        total_y += coord[1]
    
    average_x = total_x / count
    average_y = total_y / count
    
    return (average_x, average_y)
if __name__ == "__main__":
    coordinates = []
    print("Enter 2D coordinates (x y). Type 'done' when finished:")
    
    while True:
        user_input = input("Enter coordinates: ")
        if user_input.lower() == 'done':
            break
        try:
            x, y = map(float, user_input.split())
            coordinates.append((x, y))
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
    
    average_coordinates = calculate_average_coordinates(coordinates)
    print(f"Average Coordinates: ({average_coordinates[0]}, {average_coordinates[1]})")