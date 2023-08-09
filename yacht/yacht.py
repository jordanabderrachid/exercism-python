# Score categories.
# Change the values as you see fit.

def yacht(dice):
    prev = dice[0]
    for d in dice[1:]:
        if prev != d:
            return 0
        prev = d

    return 50

def times_maker(expected):
    def times(dice):
        res = 0
        for d in dice:
            if d == expected:
                res += expected

        return res

    return times

def dice_values(dice):
    values = {}
    for d in dice:
        v = values.get(d)
        if v == None:
            values[d] = 1
        else:
            values[d] = v + 1

    return values

def dice_sum(dice):
    sum = 0
    for d in dice:
        sum += d

    return sum

def make_combination(expected):
    def combination(dice):
        values = dice_values(dice)
        values_sorted = sorted(values.values())

        for e in expected:
            if values_sorted == e:
                return values
        
        return None
    
    return combination

def full_house(dice):
    if make_combination([[2,3]])(dice) != None:
        return dice_sum(dice)
    
    return 0

def four_of_a_kind(dice):
    c = make_combination([[1,4], [5]])(dice) 
    if c != None:
        for k, v in c.items():
            if v == 4 or v == 5:
                return 4 * k
        
    return 0

def expect_equals_sorted(expected):
    def equals_sorted(dice):
        if sorted(dice) == expected:
            return 30
        
        return 0
    
    return equals_sorted

def combine(*methods):
    def run(dice):
        for m in methods:
            if m(dice) != 0:
                return dice_sum(dice)
        
        return 0

    return run

YACHT = yacht
ONES = times_maker(1)
TWOS = times_maker(2)
THREES = times_maker(3)
FOURS = times_maker(4)
FIVES = times_maker(5)
SIXES = times_maker(6)
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = expect_equals_sorted([1,2,3,4,5])
BIG_STRAIGHT = expect_equals_sorted([2,3,4,5,6])
CHOICE = combine(YACHT, ONES, TWOS, THREES, FOURS, FIVES, SIXES, FULL_HOUSE, FOUR_OF_A_KIND, LITTLE_STRAIGHT, BIG_STRAIGHT)

def score(dice, category):
    return category(dice)
