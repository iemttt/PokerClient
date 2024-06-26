"""Game specific constants."""

START_BALANCE = 1000
CARDS_ON_TABLE = 5
CARDS_ON_HAND = 2
AMOUNT_RANKS = 13
AMOUNT_SUITS = 4
ALL_CARDS = [(rank, suit) for rank in range(AMOUNT_RANKS) for suit in range(AMOUNT_SUITS)]
COMBINATIONS = ["High Card", "Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush",
                "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["S", "H", "D", "C"]
