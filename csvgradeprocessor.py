# A program that reads a CSV file containing student names and grades, then calculates the average grade.

import csv

def process_grades(filename):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            
            scores = []
            for row in reader:
                try:
                    score = int(row['score'])
                    scores.append(score)
                except ValueError:
                    print(f"Invalid score for {row['name']}: {row['score']}")
            
            if not scores:
                print("No valid scores found.")
                return
            
            # Calculate average
            average = sum(scores) / len(scores)
            
            # Find highest and lowest
            highest = max(scores)
            lowest = min(scores)
            
            print(f"Average Score: {average:.2f}")
            print(f"Highest Score: {highest}")
            print(f"Lowest Score: {lowest}")
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Run the program
process_grades("grades.csv")
