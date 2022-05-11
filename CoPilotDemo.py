print("Hello World")

def calculateDaysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.    The first date is
    assumed to be earlier than the second.
    """
    # Calculate the number of days in each month
    daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Check if the first date is in a leap year
    if year1 % 4 == 0:
        daysInMonths[1] = 29
    # Calculate the number of days between the two dates
    daysBetween = 0
    # Loop through the months
    for i in range(month1 - 1, month2 - 1):
        daysBetween += daysInMonths[i]
    # Add the number of days in the first month
    daysBetween += day2
    # Subtract the number of days in the second month
    daysBetween -= day1
    # Return the number of days between the two dates
    return daysBetween

print(calculateDaysBetweenDates(2022, 1, 1, 2022, 3, 1))