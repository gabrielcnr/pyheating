class Boiler(object):
    ON = 'ON'
    OFF = 'OFF'

    def __init__(self):
        self._status = self.OFF

    @property
    def status(self):
        return self._status

    def turn_on(self):
        self._status = self.ON

    def turn_off(self):
        self._status = self.OFF
