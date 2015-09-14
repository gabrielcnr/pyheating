from pyheating import Boiler


def test_boiler_can_be_turned_on():
    boiler = Boiler()
    assert boiler.status == Boiler.OFF
    boiler.turn_on()

    assert boiler.status == Boiler.ON


def test_boiler_can_be_turned_off():
    boiler = Boiler()
    boiler.turn_on()
    assert boiler.status == Boiler.ON

    boiler.turn_off()
    assert boiler.status == Boiler.OFF
