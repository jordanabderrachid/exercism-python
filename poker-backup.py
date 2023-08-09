from abc import ABC, abstractmethod
from enum import Enum
import re

class Suit(Enum):
    CLUB = "C"
    DIAMOND = "D"
    SPADE = "S"
    HEART = "H"

class Kind(Enum):
    TWO = "2"
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "J"  # 11
    QUEEN = "Q" # 12
    KING = "K"  # 13
    ACE = "A"   # 14

def kind_rank(k):
    if k == Kind.ACE:
        return 14

    if k == Kind.KING:
        return 13
    
    if k == Kind.QUEEN:
        return 12
    
    if k == Kind.JACK:
        return 11
    
    return int(k.value)

class RankType(Enum):
    STRAIGHT_FLUSH = 10
    FOUR_OF_A_KIND = 9
    FULL_HOUSE = 8
    FLUSH = 7
    STRAIGHT = 6
    THREE_OF_A_KIND = 5
    TWO_PAIR = 4
    ONE_PAIR = 3
    HIGH_CARD = 2

class Card:
    def __init__(self, serialized):
        match = re.match(r'^(.{1,2}){1}(C|D|S|H){1}$', serialized)
        self.kind = Kind(match.group(1))
        self.suit = Suit(match.group(2))

class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.suits = self._suits(cards)
        self.kinds = self._kinds(cards)

    def _suits(self, cards):
        s = {}
        for c in cards:
            count = s.get(c.suit)
            if count == None:
                s[c.suit] = 1
            else:
                s[c.suit] = count + 1
        return s
    
    def _kinds(self, cards):
        k = {}
        for c in cards:
            count = k.get(c.kind)
            if count == None:
                k[c.kind] = 1
            else:
                k[c.kind] = count + 1
        return k

    def ranks(self):
        return sorted([HighCard(c) for c in self.cards], key=lambda c: c.rank_value())
    
    def serialize(self):
        return " ".join([f"{c.kind.value}{c.suit.value}" for c in self.cards])

class Rank(ABC):
    @abstractmethod
    def rank_type(self):
        pass

    @abstractmethod
    def rank_value(self):
        pass

class HighCard(Rank):
    def __init__(self, card):
        self.card_kind_rank = kind_rank(card.kind)
    
    def rank_type(self):
        return RankType.HIGH_CARD
    
    def rank_value(self):
        return self.card_kind_rank

def best_hands(hands_str):
    hands = list()
    for h in hands_str:
        cards = list()
        for c_str in h.split(" "):
            cards.append(Card(c_str))
        hands.append(Hand(cards))
    
    return [h.serialize() for h in hands]
