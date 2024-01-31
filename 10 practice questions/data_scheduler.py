"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""


def date_passed(todays_date, scheduled_date):
    # Your code goes here
    # Implement the logic to compare the dates and print the appropriate message
    pass  # Delete this after implementing some code inside this function

from datetime import datetime

def date_passed(todays_date, scheduled_date):
    # Function to parse the date string
    def parse_date(date_str):
        # Adding an arbitrary year for comparison
        date_str += " 2020"
        # Parse the date
        return datetime.strptime(date_str, "%dth %B %Y")

    # Parse both dates
    todays_date_parsed = parse_date(todays_date)
    scheduled_date_parsed = parse_date(scheduled_date)

    # Compare and print the appropriate message
    if todays_date_parsed > scheduled_date_parsed:
        print("Scheduled date has passed")
    elif todays_date_parsed < scheduled_date_parsed:
        print("Scheduled date is yet to pass")
    else:
        print("Scheduled date is today")
        
# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
