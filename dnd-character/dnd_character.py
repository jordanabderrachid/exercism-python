class Character:
    def __init__(self):
        self.strength = 4
        self.dexterity = 4
        self.constitution = 4
        self.intelligence = 4
        self.wisdom = 4
        self.charisma = 4
        self.hitpoints = 10 + modifier(4)

    def ability(self):
        return 4

def modifier(c):
    return (c - 10) // 2