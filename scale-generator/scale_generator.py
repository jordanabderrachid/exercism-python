scale = [
    ["A"],
    ["A#", "Bb"],
    ["B"],
    ["C"],
    ["C#", "Db"],
    ["D"],
    ["D#", "Eb"],
    ["E"],
    ["F"],
    ["F#", "Gb"],
    ["G"],
    ["G#", "Ab"],
]

sharps = ["C", "a", "G", "D", "A", "E", "B", "F#", "e", "b", "f#", "c#", "g#", "d#"]
flats = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]


class Scale:
    def __init__(self, tonic):
        self.signature = key_signature(tonic)
        for i, notes in enumerate(scale):
            if capitalize(tonic) in notes:
                self.index = i

    def chromatic(self):
        return self.interval("mmmmmmmmmmm")

    def interval(self, intervals):
        res = []
        for interval in intervals:
            res.append(self._current_note())
            if interval == "m":
                self.index += 1
            elif interval == "M":
                self.index += 2
            elif interval == "A":
                self.index += 3

        res.append(self._current_note())

        return res

    def _current_note(self):
        self.index = self.index % len(scale)
        notes = scale[self.index]
        if len(notes) == 1 or self.signature == "sharp":
            return notes[0]

        return notes[1]


def key_signature(tonic):
    if tonic in sharps:
        return "sharp"
    elif tonic in flats:
        return "flat"

    raise ValueError("invalid signature for key", tonic)


def capitalize(tonic):
    letters = list(tonic)

    if len(letters) == 1:
        return "".join([letters[0].upper()])

    return "".join([letters[0].upper(), letters[1]])
