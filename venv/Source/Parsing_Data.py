from datetime import time
import calendar
import re

#Get time or get a Value Error 
def getTime(timeGiven):
    hours, minutes = [int(i) for i in re.split(":| |H|h", timeGiven)]
    return time(hours, minutes)

#Get Day or get a Value Error
def getDay(date):
    day, month, year = [int(i) for i in re.split(" |-|/", date)]
    dayNumber = calendar.weekday(year, month, day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return (days[dayNumber])

#Get last digit of license plate or Rise a Value Error Exception if license plate isnt similar to abc1234 or DEF5678
def getLastDigitLicPlate(licPlate):
    if len(licPlate) == 7:
        if not licPlate[0:3].isalpha():
            raise ValueError("Wrong License Plate")
        if not licPlate[3::].isdigit():
            raise ValueError("Wrong License Plate")
        return int(licPlate[3::]) % 10
    else:
        raise ValueError("Wrong License Plate")

