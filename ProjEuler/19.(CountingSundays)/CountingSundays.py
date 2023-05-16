import datetime

# Set the start date to 1 Jan 1901
start_date = datetime.date(1901, 1, 1)

# Set the end date to 31 Dec 2000
end_date = datetime.date(2000, 12, 31)

# Initialize a counter to keep track of Sundays on the first of the month
sunday_counter = 0

# Iterate over each month and year
current_date = start_date
while current_date <= end_date:
    # Check if the day is a Sunday and the day of the month is 1
    if current_date.weekday() == 6 and current_date.day == 1:
        sunday_counter += 1

    # Move to the next month
    if current_date.month == 12:
        current_date = current_date.replace(year=current_date.year + 1, month=1)
    else:
        current_date = current_date.replace(month=current_date.month + 1)

print("Number of Sundays that fell on the first of the month during the twentieth century:", sunday_counter)
