# A program that calculates a user’s remaining budget after expenses, using variables for income and expenses.

import math

salary = float(input("Enter your monthly salary:"))
rent = float(input("Enter your monthly rent expense:"))
utilities = float(input("Enter your monthly utilities expense:"))
food = float(input("Enter your monthly food expense:"))
transport = float(input("Enter your monthly transport expenses: "))
total_expenses = rent + utilities + food + transport
savings = salary - total_expenses

percent_savings = (savings / salary) * 100 if salary != 0 else 0
print(f"Monthly Salary: Ksh.{salary}")
print(f"Total Expenses: Ksh.{total_expenses}")
print(f"Remaining Budget (Savings): Ksh.{savings}")
print(f"Percentage of Income Saved: {percent_savings}%")