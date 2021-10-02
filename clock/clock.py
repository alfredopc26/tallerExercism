class Clock:
    def __init__(self, hour, minute):
       self.hour = self.minute = 0
       self.__add__(minute + hour * 60)

    def __str__(self):
        return "%s:%s" % (str(self.hour).rjust(2, '0'), str(self.minute).rjust(2, '0'))

    def __eq__(self, other):
        return isinstance(other, Clock) and self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        self.minute += minutes
        self._adjust_rollover()
        return self

    def _adjust_rollover(self):
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        while self.minute < 0:
            self.minute += 60
            self.hour -= 1
        while self.hour >= 24:
            self.hour -= 24
        while self.hour < 0:
            self.hour += 24
