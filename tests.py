#!/usr/bin/env python3
import unittest
from blackjack import make_shuffled_deck
from blackjack import get_card_value
from blackjack import calculate_hand


class TestBlackjack(unittest.TestCase):

    def test_card_deck_shuffling(self):
        """
        Testing generation of the card deck. 
        """
        print('Testing card deck generation.')
        shuffled_deck = make_shuffled_deck()

        # checking for length of card deck
        self.assertEqual(len(shuffled_deck), 52)

        # checking for correct cards in the deck
        for card in [str(x) for x in range(2, 11, 1)] + ['J', 'Q', 'K', 'A']:
            self.assertEqual(shuffled_deck.count(card), 4)

    def test_card_value(self):
        print('Testing card -> value conversion.')
        """
        Testing the conversion of a card to its value. 
        """
        self.assertEqual(get_card_value('2'), 2)
        self.assertEqual(get_card_value('3'), 3)
        self.assertEqual(get_card_value('4'), 4)
        self.assertEqual(get_card_value('5'), 5)
        self.assertEqual(get_card_value('6'), 6)
        self.assertEqual(get_card_value('7'), 7)
        self.assertEqual(get_card_value('8'), 8)
        self.assertEqual(get_card_value('9'), 9)
        self.assertEqual(get_card_value('10'), 10)
        self.assertEqual(get_card_value('J'), 10)
        self.assertEqual(get_card_value('Q'), 10)
        self.assertEqual(get_card_value('K'), 10)
        self.assertEqual(get_card_value('A'), [1, 11])

    def test_hand_score(self):
        """
        Testing function to calculate the score of a given hand. 
        """
        print('Testing hand score calculation.')

        # cases with no aces
        self.assertEqual(calculate_hand(['2']), 2)
        self.assertEqual(calculate_hand(['7']), 7)
        self.assertEqual(calculate_hand(['J']), 10)
        self.assertEqual(calculate_hand(['Q']), 10)
        self.assertEqual(calculate_hand(['K']), 10)
        self.assertEqual(calculate_hand(['10']), 10)
        self.assertEqual(calculate_hand(['2', '2']), 4)
        self.assertEqual(calculate_hand(['K', '2']), 12)
        self.assertEqual(calculate_hand(['K', 'Q', '3']), 23)
        self.assertEqual(calculate_hand(['4', '6', '10']), 20)
        self.assertEqual(calculate_hand(['2', '9', '10']), 21)

        # cases with 1 ace
        self.assertEqual(calculate_hand(['A']), 11)
        self.assertEqual(calculate_hand(['A', '5']), 16)
        self.assertEqual(calculate_hand(['A', '9']), 20)
        self.assertEqual(calculate_hand(['A', 'K']), 21)
        self.assertEqual(calculate_hand(['A', 'K', '6']), 17)
        self.assertEqual(calculate_hand(['K', '6', 'A']), 17)
        self.assertEqual(calculate_hand(['K', 'K', 'A']), 21)
        self.assertEqual(calculate_hand(['K', 'K', 'A', '5']), 26)

        # cases with multiple aces
        self.assertEqual(calculate_hand(['A', 'A']), 12)
        self.assertEqual(calculate_hand(['A', 'A', '5']), 17)
        self.assertEqual(calculate_hand(['A', 'A', 'J']), 12)
        self.assertEqual(calculate_hand(['A', 'A', 'J', 'A']), 13)
        self.assertEqual(calculate_hand(['A', 'A', 'J', 'A', 'K']), 23)


if __name__ == '__main__':
    unittest.main()
