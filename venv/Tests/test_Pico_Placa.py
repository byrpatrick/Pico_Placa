import Source.Pico_Placa as pp
import pytest
from datetime import time

@pytest.mark.parametrize("lastDigit, day, timeGiven, result", 
                         [(5, "Wednesday", time(7, 30), "The car can't be on road.")
                          ])
def test_canBeOnRoad(lastDigit, day, timeGiven, result):
    assert pp.canBeOnRoad(lastDigit, day, timeGiven) == result