#part a
def get_days_in_month(month):
    if month == "January":
        return 31
    elif month == "February":
        return 28
    elif month == "March":
        return 31
    elif month == "April":
        return 30
    elif month == "May":
        return 31
    elif month == "June":
        return 30
    elif month == "July":
        return 31
    elif month == "August":
        return 31
    elif month == "September":
        return 30
    elif month == "October":
        return 31
    elif month == "November":
        return 30
    elif month == "December":
        return 31
    else:
        return -1  

#part b
def isLeapYear(year):
    leap = False
    if(year%4 == 0 and year%100 != 0):
        leap = True
    elif(year %400 == 0):
        leap =  True

    else:
        leap = False
    
    return leap

#part c
def elapsed_time(hour1, min1, hour2, min2):
    minutes1 = hour1 * 60 + min1
    minutes2 = hour2 * 60 + min2
    return abs(minutes2 - minutes1)

#part d

def thanksgiving_date(first_day_january):
    days_in_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    jan1_day = days_in_week.index(first_day_january)
    days_to_thanksgiving = 4 - jan1_day + 26
    if days_to_thanksgiving <= 28:
        return ("November" + str(days_to_thanksgiving))
    else:
        return ("November" + str(days_to_thanksgiving - 7))
