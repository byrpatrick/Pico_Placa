import Source.Pico_Placa as pp
import pytest

def test_canBeOnRoad():
    assert pp.canBeOnRoad(7, "Thursday", "7:00") == "The car can be on road."