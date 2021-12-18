import random
from art import logo

def deal_card():
    """ Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)  # process to randomly select within the given choices
    return card


def calculate_score(cards):
    """ Take a list of cards and return teh score calculated from cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "its a draw"
    elif computer_score == 0:
        return "oops`! you lost. the opponent has Blackjack!!!"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():

    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Create a function called calculate_score() that takes a List of cards as input
    # and returns the score.
    # Look up the sum() function to help you do this
    # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

    for _ in range(2):
        # new_card = deal_card()
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(cards=user_cards)
        computer_score = calculate_score(cards=computer_cards)

        print(f"your cards: {user_cards}, score: {user_score}\ncomputer card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card and type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(cards=computer_cards)

    print(f" Your final hand = {user_score} \nYour Opponent's final hand - {computer_score} ")
    print(compare(user_score=user_score, computer_score=computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
