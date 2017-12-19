def days_in_month(name):
    """takes a month name and returns the number of days in that month"""
    if name == "January" or name == "March" or name == "May" or name == "July" or name == "August" or name == "October" or name == "December":
        return 31
    elif name == "February":
        return 28
    elif name == "April" or name == "June" or name == "November":
        return 30


print("\ndays_in_month")
test(days_in_month("February") == 28)
test(days_in_month("December") == 31)

