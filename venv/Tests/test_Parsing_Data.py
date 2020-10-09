import Source.Parsing_Data as pd
import pytest
from datetime import time

def test_getTime():
    assert pd.getTime("16:30") == time(16, 30)

def test_getTime_ValueError():
    with pytest.raises(ValueError):
        pd.getTime("25:30")

def test_getDay():
    assert pd.getDay("07-10-2020") == "Wednesday"

def test_getDay_ValueError():
    with pytest.raises(ValueError):
        pd.getDay("13-13-2020")
        
def test_getLastDigitLicPlate():
    assert pd.getLastDigitLicPlate("ABC5612") == 2
    
def test_getLastDigitLicPlate_ValueError():
    with pytest.raises(ValueError):
        pd.getLastDigitLicPlate("as23344")