from typing import List

default_students = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
]


names_mapping = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}


def convert_plant_names(names: List[str]) -> List[str]:
    return [names_mapping.get(n) for n in names]


class Garden:
    def __init__(self, diagram: str, students=default_students):
        lines = diagram.splitlines()
        self.first_row = list(lines[0])
        self.second_row = list(lines[1])
        self.students = list(sorted(students))

    def plants(self, student) -> List[str]:
        i = self.students.index(student)
        return convert_plant_names(
            [
                self.first_row[2 * i],
                self.first_row[2 * i + 1],
                self.second_row[2 * i],
                self.second_row[2 * i + 1],
            ]
        )
