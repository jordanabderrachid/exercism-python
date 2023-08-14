class School:
    def __init__(self):
        self._added = []
        self._roaster = []
        self._names = []

    def add_student(self, name, grade):
        s = (name, grade)
        try:
            self._names.index(name)
            self._added.append(False)
        except ValueError:
            self._added.append(True)
            self._roaster.append(s)
            self._names.append(name)
            self._roaster = sorted(self._roaster, key=lambda s: (s[1], s[0]))

    def roster(self):
        return [s[0] for s in self._roaster]

    def grade(self, grade_number):
        return [s[0] for s in self._roaster if s[1] == grade_number]

    def added(self):
        return self._added
