"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if len(list_one) == len(list_two):
        for i in range(len(list_one)):
            if list_one[i] != list_two[i]:
                return UNEQUAL
        return EQUAL
    elif len(list_one) < len(list_two):
        for i in range(len(list_two)):
            if i + len(list_one) > len(list_two):
                return UNEQUAL
            
            if sublist(list_one, list_two[i:i+len(list_one)]) == EQUAL:
                return SUBLIST
        return UNEQUAL     
    else:
        if sublist(list_two, list_one) == SUBLIST:
            return SUPERLIST
        return UNEQUAL