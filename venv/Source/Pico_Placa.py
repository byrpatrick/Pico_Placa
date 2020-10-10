from datetime import time
import calendar

def getDay(date):
    dayNumber = calendar.weekday(date.year, date.month, date.day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return (days[dayNumber])

class Pico_Placa():
    def __init__(self,
                 rulesPP = {"Monday":[1,2], "Tuesday":[3,4], "Wednesday":[5,6], "Thursday":[7,8], "Friday":[9,0]},
                 picoHours = [[time(7, 0), time(9, 30)],[time(16, 0), time(19, 30)]]
                 ):
        self.__rulesPP = rulesPP
        self.__picoHours = picoHours

    def isPicoHour(self, timeGiven):
        for picoH in self.__picoHours:
            if (timeGiven >= picoH[0] and timeGiven <= picoH[1]):
                return True
        return False

    def canBeOnRoad(self, lastDigit, date, timeGiven):
        day = getDay(date)
        # It's weekend anyone can be on road, enjoy your journey!!
        if day in ["Saturday", "Sunday"]:
            return "The car can be on road."
        # When the time is right, you can drive!!
        # If isn't a pico hour you can drive.
        if not self.isPicoHour(timeGiven):
            return "The car can be on road."
        # Isn't weekend and is a pico hour. Can I drive?
        for k, v in self.__rulesPP.items():
            if (day == k) and (lastDigit in v):
                return "The car can't be on road."
        return "The car can be on road."

