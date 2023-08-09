from abc import ABC, abstractmethod
from enum import Enum
from typing import List
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
    QUEEN = "Q"  # 12
    KING = "K"  # 13
    ACE = "A"  # 14


def kind_rank(k: Kind) -> int:
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


class Rank(ABC):
    @abstractmethod
    def rank_type(self) -> RankType:
        pass

    @abstractmethod
    def rank_value(self) -> int:
        pass


class Card:
    def __init__(self, serialized):
        match = re.match(r"^(.{1,2}){1}(C|D|S|H){1}$", serialized)
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
            if count is None:
                s[c.suit] = 1
            else:
                s[c.suit] = count + 1
        return s

    def _kinds(self, cards):
        k = {}
        for c in cards:
            count = k.get(c.kind)
            if count is None:
                k[c.kind] = 1
            else:
                k[c.kind] = count + 1
        return k

    def ranks(self) -> List[Rank]:
        r = []

        pair_kinds = list()
        for kind, count in self.kinds.items():
            if count == 2:
                pair_kinds.append(kind)
            if count == 3:
                r.append(ThreeOfAKind(kind))

        if len(pair_kinds) == 2:
            r.append(TwoPair(pair_kinds[0], pair_kinds[1]))

        for kind in pair_kinds:
            r.append(OnePair(kind))

        r += sorted([HighCard(c) for c in self.cards], key=lambda c: -c.rank_value())
        return r

    def highest_rank_type(self) -> Rank:
        return sorted(self.ranks(), key=lambda r: -r.rank_type().value)[0]

    def serialize(self) -> str:
        return " ".join([f"{c.kind.value}{c.suit.value}" for c in self.cards])


class HighCard(Rank):
    def __init__(self, card):
        self.card_kind_rank = kind_rank(card.kind)

    def rank_type(self) -> RankType:
        return RankType.HIGH_CARD

    def rank_value(self) -> int:
        return self.card_kind_rank


class OnePair(Rank):
    def __init__(self, kind):
        self.card_kind_rank = kind_rank(kind)

    def rank_type(self) -> RankType:
        return RankType.ONE_PAIR

    def rank_value(self) -> int:
        return self.card_kind_rank


class TwoPair(Rank):
    def __init__(self, first_kind, second_kind):
        self.card_kind_rank = max(kind_rank(first_kind), kind_rank(second_kind))

    def rank_type(self) -> RankType:
        return RankType.TWO_PAIR

    def rank_value(self) -> int:
        return self.card_kind_rank


class ThreeOfAKind(Rank):
    def __init__(self, kind):
        self.card_kind_rank = kind

    def rank_type(self) -> RankType:
        return RankType.THREE_OF_A_KIND

    def rank_value(self) -> int:
        return self.card_kind_rank


def best_hands(hands_str):
    hands: List[Hand] = list()
    for h in hands_str:
        cards = list()
        for c_str in h.split(" "):
            cards.append(Card(c_str))
        hands.append(Hand(cards))

    highest_rank_type_value = None
    to_keep = []
    for h in hands:
        if highest_rank_type_value is None:
            highest_rank_type_value = h.highest_rank_type().rank_type().value
            to_keep = [h]
        elif highest_rank_type_value == h.highest_rank_type().rank_type().value:
            to_keep.append(h)
        elif highest_rank_type_value < h.highest_rank_type().rank_type().value:
            highest_rank_type_value = h.highest_rank_type().rank_type().value
            to_keep = [h]
    hands = to_keep

    has_more_rank = True
    rank_index = 0
    while len(hands) > 1 and has_more_rank:
        highest_rank_value = None
        hands_to_keep = []
        for h in hands:
            rank = h.ranks()[rank_index]
            r_v = rank.rank_value()
            if highest_rank_value is None:
                hands_to_keep = [h]
                highest_rank_value = r_v
            elif r_v == highest_rank_value:
                hands_to_keep.append(h)
            elif r_v > highest_rank_value:
                hands_to_keep = [h]
                highest_rank_value = r_v

        hands = hands_to_keep
        rank_index += 1
        has_more_rank = rank_index < len(hands[0].ranks())

    return [h.serialize() for h in hands]
