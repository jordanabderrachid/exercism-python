scores = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128
}

class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        item_score = scores[item]
        return ((self.score & item_score) ^ item_score) == 0

    @property
    def lst(self):
        l = list()
        for allergy in scores:
            if self.allergic_to(allergy):
                l.append(allergy)

        return l
