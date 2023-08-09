import random

# generate a random integer between 0 and 9
random_int = random.randint(0, 9)


class Robot:
    allocated_names = set()

    def __init__(self):
        self.name = Robot._random_name()

    def _random_name():    
        name = f"{random_letter()}{random_letter()}{random_digit()}{random_digit()}{random_digit()}"
        if name in Robot.allocated_names:
            return Robot._random_name()
    
        Robot.allocated_names.add(name)
        return name

    def reset(self):
        self.name = Robot._random_name()

def random_letter():
    return chr(random.randint(65, 90))

def random_digit():
    return chr(random.randint(48, 57))