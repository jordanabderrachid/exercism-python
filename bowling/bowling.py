class Frame:
    def __init__(self, pin, is_10th_frame: False):
        if not (0 <= pin <= 10):
            raise ValueError("pin must be between 0 and 10")

        self.pins = [pin]
        self._is_10th_frame = is_10th_frame

    def is_strike(self):
        if not self._is_10th_frame:
            return len(self.pins) == 1 and sum(self.pins) == 10

        return self.pins[-1] == 10

    def is_spare(self):
        if not self._is_10th_frame:
            return len(self.pins) == 2 and sum(self.pins) == 10

        return False

    def is_closed(self):
        if not self._is_10th_frame:
            return self.is_strike() or len(self.pins) == 2

        if self.pins[0] == 10:
            return len(self.pins) >= 3

        if len(self.pins) == 2 and sum(self.pins) == 10:
            return False

        return len(self.pins) >= 2

    def add_pin(self, pin):
        if not (0 <= pin <= 10):
            raise ValueError("pin must be between 0 and 10")

        if self.is_closed():
            raise ValueError("this frame is closed")

        if not self._is_10th_frame and sum(self.pins) + pin > 10:
            raise ValueError("this pin is too high")

        if self._is_10th_frame and not self.is_strike():
            if self.pins[0] == 10:
                if (sum(self.pins) - 10) + pin > 10:
                    raise ValueError("this pin is too high")

        self.pins.append(pin)


class BowlingGame:
    def __init__(self):
        self._frames = []

    def roll(self, pin):
        if self._is_complete():
            raise ValueError("game is complete")

        if len(self._frames) == 0 or self._frames[-1].is_closed():
            self._frames.append(Frame(pin, is_10th_frame=len(self._frames) == 9))
        else:
            self._frames[-1].add_pin(pin)

    def _is_complete(self):
        return len(self._frames) == 10 and self._frames[-1].is_closed()

    def score(self):
        if not self._is_complete():
            raise ValueError("game is not complete")

        score = sum([sum(f.pins) for f in self._frames])
        for i in range(len(self._frames) - 1):
            f = self._frames[i]
            if f.is_strike():
                next_frame = self._frames[i + 1]
                pins = next_frame.pins.copy()
                if len(pins) < 2:
                    pins += self._frames[i + 2].pins

                score += sum(pins[0:2])

            if f.is_spare():
                score += self._frames[i + 1].pins[0]

        return score
