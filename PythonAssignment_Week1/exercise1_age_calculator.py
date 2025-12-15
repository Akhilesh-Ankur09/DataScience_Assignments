# -------------------------------------------------
# Exercise 1: Age Calculator
# -------------------------------------------------
# This program:
# 1. Accepts birth date in mm/dd/yyyy format
# 2. Validates the date format and correctness
# 3. Calculates current age in years
# 4. Displays birth date in European format (dd/mm/yyyy)
# 5. Handles all errors gracefully
# -------------------------------------------------

from datetime import datetime

try:
    # Ask the user to enter birth date
    birth_input = input("Enter your birth date (mm/dd/yyyy): ")

    # Convert string input to datetime object
    birth_date = datetime.strptime(birth_input, "%m/%d/%Y")

    # Get today's date
    today = datetime.today()

    # Calculate age in years
    age = today.year - birth_date.year

    # Adjust age if birthday has not occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    # Convert birth date to European format
    european_date = birth_date.strftime("%d/%m/%Y")

    # Display results
    print("\nAge Calculation Result")
    print("----------------------")
    print(f"Birth date (European format): {european_date}")
    print(f"Current age: {age} years")

except ValueError:
    # Handles invalid date formats or impossible dates
    print("Error: Please enter a valid date in mm/dd/yyyy format.")

except Exception as e:
    # Handles any unexpected errors
    print("An unexpected error occurred:", e)
