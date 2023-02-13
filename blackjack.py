#!/usr/bin/env python3
import random


def main():
    play_game()


def make_shuffled_deck() -> list:
    """
    Function that creates a shuffled card deck. 

    Output(list): 
        list of 52 cards in a randomized order
    """
    full_deck = ([str(x) for x in range(2, 11, 1)] + ['J', 'Q', 'K', 'A']) * 4

    # multiple shuffles
    for i in range(3):
        random.shuffle(full_deck)
    return full_deck


def calculate_hand(hand: list) -> int:
    """
    Function that calculates the score of a given hand. 

    Inputs: 
        hand(list): list of cards in a given hand. 

    Output (int): 
        score of the hand
    """
    score = 0
    ace_count = 0
    for card in hand:
        if card != 'A':
            score += get_card_value(card)
        else:
            ace_count += 1

    # handling the aces
    if ace_count > 0 and score + 11 + ace_count - 1 <= 21:
        return score + 11 + ace_count - 1
    else:
        return score + ace_count


def get_card_value(card: str):
    """
    Function that returns the value of a given card

    Inputs: 
        card(str): a given card whose value we need

    Output(int or list): 
        value of the card
    """
    if card in [str(x) for x in range(1, 11, 1)]:
        return int(card)
    elif card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return [1, 11]


def play_game():
    """
    Function which contains the game state and logic. 
    """

    # dealing cards
    card_deck = make_shuffled_deck()

    dealer_hand = []
    player_hand = []

    for i in range(2):
        player_hand.append(card_deck.pop())
        dealer_hand.append(card_deck.pop())

    players_turn = True
    dealers_turn = False

    dealer_score = calculate_hand(dealer_hand)
    player_score = calculate_hand(player_hand)

    # player's turn
    while players_turn:
        print_game_state(player_hand, dealer_hand,
                         players_turn, player_score, dealer_score)

        if player_score > 21:  # player busts
            print('\nPlayer busts with ', player_score)
            print('Dealer wins')
            return
        elif player_score == 21:  # blackjack; player wins
            print('\nPlayer Wins!', 'Blackjack!')
            return
        else:   # player needs to make a choice

            player_choice = prompt_player()

            if player_choice == 'H':  # player HITS
                print('\nPlayer Hits.')
                player_hand.append(card_deck.pop())
                player_score = calculate_hand(player_hand)

            else:  # player STANDS
                print_player_stands(player_hand, player_score)
                players_turn = False
                dealers_turn = True

    # dealer's turn
    while dealers_turn:
        print_dealer_state(dealer_hand, dealer_score)
        if dealer_score > 21:  # dealer busts
            print('Dealer busts.\n\nPlayer wins!')
            return
        elif dealer_score == 21:  # dealer hits blackjack
            print('Blackjack! Dealer wins.')
            return
        elif dealer_score < 17:  # dealer hits
            print('Dealer hits.')
            dealer_hand.append(card_deck.pop())
            dealer_score = calculate_hand(dealer_hand)
        else:  # dealer stands
            dealers_turn = False

    # evaluating the end of the game (if no one busts)
    print_game_state(player_hand, dealer_hand,
                     players_turn, player_score, dealer_score)
    evaluate_game_result(player_hand, player_score, dealer_hand, dealer_score)


def prompt_player():
    """Function to get player input, Hit or Stand. Returns the player's choice."""
    command = input('Would you like to (H)it or (S)tand? ')
    while command.upper() not in ['S', 'H']:
        command = input("Invalid Input ... Enter 'S' to stand or 'H' to Hit: ")
    return command.upper()


def print_game_state(player_hand: list, dealer_hand: list, player_turn: bool, player_score: int, dealer_score: int):
    """Function that takes in the game state and prints it in a proper format."""
    if player_turn:
        print("\nDealer has: {first_card} ? = ?".format(
            first_card=dealer_hand[0]))

    else:
        dealer_str = '\nDealer has: ' +  \
            get_hand_string(dealer_hand, dealer_score)
        print(dealer_str)

    player_str = 'Player has: ' + get_hand_string(player_hand, player_score)
    print(player_str)


def print_player_stands(player_hand, player_score):
    """ 
    Function to print the start of the game when player stands. 
    """
    player_str = "\nPlayer stands with: " + \
        get_hand_string(player_hand, player_score)
    print(player_str)


def print_dealer_state(dealer_hand, dealer_score):
    """
    Function to print the dealer's state of the game on the dealer's turn. 
    """
    dealer_str = '\nDealer\'s hand: ' + \
        get_hand_string(dealer_hand, dealer_score)
    print(dealer_str)


def evaluate_game_result(player_hand, player_score, dealer_hand, dealer_score):
    """
    Function to evaluate the outcome of the game. 

    """
    if dealer_score > player_score:
        print('\nDealer Wins.')
        print(get_hand_string(dealer_hand, dealer_score) +
              ' to Player\'s ' + get_hand_string(player_hand, player_score))
        return 'Dealer'
    elif player_score > dealer_score:
        print('\nPlayer Wins.')
        print(get_hand_string(player_hand, player_score) +
              ' to Dealer\'s ' + get_hand_string(dealer_hand, dealer_score))
        return 'Player'
    else:
        print('\nTie!')
        print('Player\'s ' + get_hand_string(player_hand, player_score) +
              ' to Dealer\'s ' + get_hand_string(dealer_hand, dealer_score))
        return 'Tie'


def get_hand_string(hand: list, score: int) -> str:
    """Function that takes a hand and score and outputs its string representation."""
    hand_str = ""
    for card in hand:
        hand_str += card + ' '
    hand_str += '= ' + str(score)
    return hand_str


if __name__ == "__main__":
    main()
