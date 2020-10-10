import Source.Parsing_Data as pd
import Source.Pico_Placa as pp

info = """Welcome to Pico & Placa Predictor:\n
          Format Plate Number Example: ABC0291\n
          Format Date: DD-MM-YYYY or DD/MM/YYYY or DD MM YYYY\n
          Formate Time: HH:MM or HH MM or HHhMM"""

print(info)
while True:
    try:
        licensePlate = input("Enter a license plate number: ")
        lastDigitLicPlate = pd.getLastDigitLicPlate(licensePlate)
        break
    except ValueError:
        print("Please, type a valid license plate number!")

while True:
    try:
        date = pd.getDate(input("Enter a date: "))
        break
    except ValueError:
        print("Please, type a valid date!")

while True:
    try:
        timeGiven = pd.getTime(input("Especify a time: "))
        break
    except ValueError:
        print("Please, especify a valid time!")

objPP = pp.Pico_Placa()
print(objPP.canBeOnRoad(lastDigitLicPlate, date, timeGiven))

