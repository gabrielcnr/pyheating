from pyheating import Boiler


class HeatController(object):
    """
    The Main Controller Unit.

    It has the responsibility to turn ON and OFF the Boiler
    and be the point of contact for the TRV's.
    """

    def __init__(self, boiler=None):
        self._boiler = boiler or Boiler()
        self._trv_units = set()
        self._trv_sequence_id = 0

    def get_boiler_status(self):
        return self._boiler.status

    def turn_boiler_on(self):
        self._boiler.turn_on()

    def turn_boiler_off(self):
        self._boiler.turn_off()

    @property
    def trv_units(self):
        return self._trv_units

    def add_trv(self, trv):
        self._trv_sequence_id += 1
        if trv.name is None:
            trv.name = 'TRV #{}'.format(self._trv_sequence_id)
        self._trv_units.add(trv)

    def remove_trv(self, trv):
        self._trv_units.remove(trv)
