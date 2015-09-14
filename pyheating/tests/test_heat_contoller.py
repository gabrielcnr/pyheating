from pyheating import HeatController, Boiler


def test_create_basic_heat_controller():
    controller = HeatController()
    assert controller._boiler is not None


def test_pass_boiler_as_param_on_init():
    my_boiler = Boiler()
    controller = HeatController(boiler=my_boiler)
    assert controller._boiler is my_boiler


def test_controller_can_turn_on_and_off_the_boiler():
    controller = HeatController()

    assert Boiler.OFF == controller.get_boiler_status()

    controller.turn_boiler_on()

    assert Boiler.ON == controller.get_boiler_status()

    controller.turn_boiler_off()

    assert Boiler.OFF == controller.get_boiler_status()




