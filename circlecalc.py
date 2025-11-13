# A program that calculates the area and circumference of a circle using math.pi 

import math

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

# Prompt user
radius = float(input("Enter the radius: "))

# Display results with two decimal places
print(f"Area of circle: {circle_area(radius):.2f}")
print(f"Circumference of circle: {circle_circumference(radius):.2f}")
print(f"Volume of sphere: {sphere_volume(radius):.2f}")
