from enum import Enum
from typing import List, Dict
from abc import ABC, abstractmethod


class Category(ABC):
    @abstractmethod
    def value() -> int:
        pass


class Suit(Enum):
    DIAMOND = "D"
    SPADE = "S"
    CLUB = "C"
    HEARTH = "H"


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
    JACK = "J"
    QUEEN = "Q"
    KING = "K"
    ACE = "A"


def kind_rank(k: Kind) -> int:
    kinds = [
        Kind.TWO,
        Kind.THREE,
        Kind.FOUR,
        Kind.FIVE,
        Kind.SIX,
        Kind.SEVEN,
        Kind.EIGHT,
        Kind.NINE,
        Kind.TEN,
        Kind.JACK,
        Kind.QUEEN,
        Kind.KING,
        Kind.ACE,
    ]

    return kinds.index(k) + 1


class Card:
    def __init__(self, repr: str) -> None:
        self.kind_repr = repr[0 : len(repr) - 1]
        self.kind = Kind(self.kind_repr)
        self.suit = Suit(repr[len(repr) - 1])


straight = "2345A2345678910JQKA"


class StraightFlush(Category):
    def __init__(self, straight_repr: str) -> None:
        super().__init__()
        self.straight_repr = straight_repr

    def value(self) -> int:
        return 4 * (10**6) + straight.find(self.straight_repr)


class FourOfAKind(Category):
    def __init__(self, quads: Kind, kicker: Kind) -> None:
        super().__init__()
        self.quads = quads
        self.kicker = kicker

    def value(self) -> int:
        return 3 * (10**6) + 100 * kind_rank(self.quads) + kind_rank(self.kicker)


class FullHouse(Category):
    def __init__(self, triplet: Kind, pair: Kind) -> None:
        super().__init__()
        self.triplet = triplet
        self.pair = pair

    def value(self) -> int:
        return 2 * (10**6) + 100 * kind_rank(self.triplet) + kind_rank(self.pair)


class Flush(Category):
    def __init__(self, cards: List[Card]) -> None:
        super().__init__()
        self.cards = cards

    def value(self) -> int:
        v = 0
        for i, c in enumerate(self.cards):
            v = v + kind_rank(c.kind) * (10**i)
        return 10**6 + v


class Straight(Category):
    def __init__(self, straight_repr: str) -> None:
        super().__init__()
        self.straight_repr = straight_repr

    def value(self) -> int:
        return 3000 + straight.find(self.straight_repr)


class ThreeOfAKind(Category):
    def __init__(self, k: Kind) -> None:
        super().__init__()
        self.k = k

    def value(self) -> int:
        return 2000 + kind_rank(self.k)


class TwoPair(Category):
    def __init__(self, first: Kind, second: Kind) -> None:
        super().__init__()
        self.first = kind_rank(first)
        self.second = kind_rank(second)

    def value(self) -> int:
        return (
            1000 + 100 * max([self.first, self.second]) + min([self.first, self.second])
        )


class Pair(Category):
    def __init__(self, k: Kind) -> None:
        super().__init__()
        self.k = k

    def value(self) -> int:
        return 100 + kind_rank(self.k)


class HighCard(Category):
    def __init__(self, c: Card):
        super().__init__()
        self.v = kind_rank(c.kind)

    def value(self) -> int:
        return self.v


class Hand:
    def __init__(self, repr: str) -> None:
        cards: List[Card] = list()
        self.repr = repr
        for card_repr in repr.split(" "):
            cards.append(Card(card_repr))

        cards.sort(key=lambda c: kind_rank(c.kind))
        self.cards = cards

    def categories(self) -> List[Category]:
        categories = list()
        kinds: Dict[Kind, int] = dict()
        suits: Dict[Suit, int] = dict()
        for c in self.cards:
            categories.append(HighCard(c))
            kind_count = kinds.get(c.kind)
            if kind_count is None:
                kinds[c.kind] = 1
            else:
                kinds[c.kind] = kind_count + 1

            suit_count = suits.get(c.suit)
            if suit_count is None:
                suits[c.suit] = 1
            else:
                suits[c.suit] = suit_count + 1

        ones = list(filter(lambda t: t[1] == 1, kinds.items()))
        fours = list(filter(lambda t: t[1] == 4, kinds.items()))
        threes = list(filter(lambda t: t[1] == 3, kinds.items()))
        for kind, _ in threes:
            categories.append(ThreeOfAKind(kind))

        pairs = list(filter(lambda t: t[1] == 2, kinds.items()))
        for kind, _ in pairs:
            categories.append(Pair(kind))

        if len(pairs) == 2:
            categories.append(TwoPair(pairs[0][0], pairs[1][0]))

        flush = list(filter(lambda t: t[1] == 5, suits.items()))
        if len(flush) > 0:
            categories.append(Flush(self.cards))

        all_kinds_repr = "".join([c.kind_repr for c in self.cards])
        if all_kinds_repr in straight:
            categories.append(Straight(all_kinds_repr))

            if len(flush) > 0:
                categories.append(StraightFlush(all_kinds_repr))

        if len(threes) > 0 and len(pairs) > 0:
            categories.append(FullHouse(threes[0][0], pairs[0][0]))

        if len(fours) > 0:
            categories.append(FourOfAKind(fours[0][0], ones[0][0]))

        return categories


class BestHandResult(Enum):
    LEFT = "L"
    RIGHT = "R"
    BOTH = "B"


def best_hand(left: Hand, right: Hand) -> BestHandResult:
    left_values = [c.value() for c in left.categories()]
    right_values = [c.value() for c in right.categories()]

    while len(left_values) > 0:
        max_l = max(left_values)
        max_r = max(right_values)

        if max_l > max_r:
            return BestHandResult.LEFT

        if max_r > max_l:
            return BestHandResult.RIGHT

        left_values.remove(max_l)
        right_values.remove(max_r)

    return BestHandResult.BOTH


def best_hands(hands_str):
    best: List[Hand] = list()
    for hand_repr in hands_str:
        h = Hand(hand_repr)
        if len(best) == 0:
            best.append(h)
        else:
            current_best = best[0]
            best_hand_result = best_hand(current_best, h)
            if best_hand_result == BestHandResult.BOTH:
                best.append(h)

            if best_hand_result == BestHandResult.RIGHT:
                best = [h]

    return [b.repr for b in best]
