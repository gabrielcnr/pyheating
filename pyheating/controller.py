from pyheating import Boiler

class HeatController(object):
    """
    The Main Controller Unit.

    It has the responsibility to turn ON and OFF the Boiler
    and be the point of contact for the TRV's.
    """

    def __init__(self, boiler=None):
        self._boiler = boiler or Boiler()
        self.units = []

    def get_boiler_status(self):
        return self._boiler.status

    def turn_boiler_on(self):
        self._boiler.turn_on()

    def turn_boiler_off(self):
        self._boiler.turn_off()




