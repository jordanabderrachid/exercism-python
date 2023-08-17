class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return (
            str(self._canonical_hour()).rjust(2, "0")
            + ":"
            + str(self._canonical_minute()).rjust(2, "0")
        )

    def __eq__(self, other):
        return (
            self._canonical_hour() == other._canonical_hour()
            and self._canonical_minute() == other._canonical_minute()
        )

    def __add__(self, minutes):
        self.minute += minutes
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        return self

    def _canonical_hour(self):
        additional_hour = self.minute // 60
        return (self.hour + additional_hour) % 24

    def _canonical_minute(self):
        return self.minute % 60
