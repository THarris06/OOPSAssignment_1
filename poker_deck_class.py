from dataclasses import dataclass


@dataclass
class Card:
    suit: str
    rank: str

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank


@dataclass
class Deck:
    deck_list = []