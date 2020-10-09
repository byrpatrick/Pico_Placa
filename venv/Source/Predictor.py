import Source.Parsing_Data as pd
import Source.Pico_Placa as pp

while True:
    try:
        licensePlate = input("Enter a license plate number: ")
        lastDigitLicPlate = pd.getLastDigitLicPlate(licensePlate)
        break
    except ValueError:
        print("Please, type a valid license plate number!")

while True:
    try:
        date = input("Enter a date: ")
        day = pd.getDay(date)
        break
    except ValueError:
        print("Please, type a valid date!")

while True:
    try:
        timeGiven = input("Especify a time: ")
        timeG = pd.getTime(timeGiven)
        break
    except ValueError:
        print("Please, especify a valid time!")

print(pp.canBeOnRoad(lastDigitLicPlate, day, timeG))
