# A program that takes a student's score as input and assigns a letter grade based on standard thresholds. 

import math

name = input("Enter the student's name:")
score = float(input("Enter the student's score (0-100%):"))

if score >= 90 and score <= 100:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
elif score >= 0 and score <= 59:
    grade = 'F'  
elif score < 0 or score > 100:
    grade = 'Invalid score'  
else:
    grade = 'Invalid score'

print(f"Student's Name: {name}, Student's Score: {score}%, Assigned Grade: {grade}")
