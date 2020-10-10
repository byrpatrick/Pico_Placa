# Pico_Placa
This application was developed using Python programming language.
Pico&Placa past rules have been considered for the development of this application:
Cars which he last digit of its license plate number cannot be on road in Pico Hours depending of the following rules:
    Day     | last digit of license plate number
- Monday:     [1,2]
- Tuesday:    [3,4]
- Wednesday:  [5,6]
- Thursday:   [7,8]
- Friday:     [9,0]

Note: Pico Hours are from 7:00 to 9:30 and from 16:00 to 19:30. Any car can be on road on weekends.

# Libraries
- Standard Python Libraries: datetime, re, calendar
- Addiotionally 3rd part library: pytest

# Use
The main file is Predictor.py, here you must insert a license plate number,  a date and a time. 
If the car is allowed to be on road the output is "The car can be on road."
If the car is not allowed to be on road the output is "The car can't be on road."

