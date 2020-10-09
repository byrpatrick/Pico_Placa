from datetime import time

rulesPicoPlaca = {"Monday":[1,2], "Tuesday":[3,4], "Wednesday":[5,6], "Thursday":[7,8], "Friday":[9,0]}

def isPicoHour(timeGiven):
    return (timeGiven >= time(7, 0) and timeGiven <= time(9, 30) or
            timeGiven >= time(16, 0) and timeGiven <= time(19, 30))

def canBeOnRoad(lastDigit, day, timeGiven):
    #It's weekend anyone can be on road, enjoy your journey!!
    if day in ["Saturday","Sunday"]:
        return "The car can be on road."
    #When the time is right, you can drive!!
    #If isn't a pico hour you can drive.
    if not isPicoHour(timeGiven):
        return "The car can be on road."
    #Isn't weekend and is a pico hour. Can I drive?
    for k, v in rulesPicoPlaca.items():
        if (day == k) and (lastDigit in v):
            return "The car can't be on road."
    return "The car can be on road."