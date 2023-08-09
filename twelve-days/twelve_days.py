def intro(verse):
    return f"On the {day_count(verse)} day of Christmas my true love gave to me"

days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
def day_count(verse):
    return days[verse-1]

gifts_list = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming"
]
def gits(start_verse):
    g = gifts_list[0:start_verse]
    g.reverse()

    if len(g) == 1:
        return g[0]
    
    return ", ".join(g[0:-1]) + f", and {g[-1]}"


def recite(start_verse, end_verse):
    verses = list()
    for i in range(start_verse, end_verse+1):
        verses.append(intro(i) + ": " + gits(i) + ".")    
    return verses
