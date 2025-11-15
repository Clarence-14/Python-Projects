# A program that calculates the number of days until a user-specified deadline using datetime.

from datetime import datetime, timedelta

def days_until_deadline(deadline_str):
    try:
        # Parse the deadline string into a datetime object
        deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        
        # Calculate the difference in days
        delta = (deadline - today).days
        
        # Check if deadline has passed
        if delta > 0:
            return f"{delta} day(s) left until the deadline."
        elif delta == 0:
            return "The deadline is today!"
        else:
            return f"The deadline passed {-delta} day(s) ago."
    
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

# --- Interactive part ---
if __name__ == "__main__":
    user_input = input("Enter your deadline (YYYY-MM-DD): ")
    result = days_until_deadline(user_input)
    print(result)
