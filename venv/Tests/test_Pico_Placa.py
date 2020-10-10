import Source.Pico_Placa as pp
import pytest
from datetime import datetime, time

objPP = pp.Pico_Placa()
@pytest.mark.parametrize("lastDigit, date, timeGiven, result",
                         [(5, datetime(2020, 10, 7), time(7, 30), "The car can't be on road."),
                          (5, datetime(2020, 10, 7), time(10, 30), "The car can be on road."),
                          (1, datetime(2020, 10, 7), time(16, 30), "The car can be on road."),
                          (1, datetime(2020, 10, 5), time(16, 30), "The car can't be on road."),
                          (1, datetime(2020, 10, 10), time(10, 30), "The car can be on road."),
                          (0, datetime(2020, 10, 9), time(8, 30), "The car can't be on road.")
                          ])
def test_canBeOnRoad(lastDigit, date, timeGiven, result):
    assert objPP.canBeOnRoad(lastDigit, date, timeGiven) == result