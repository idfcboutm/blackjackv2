import random
from turtle import color
from venv import create
try:
    import tkinter as tk
except ImportError:
    from tkinter import *


app = tk.Tk()
app.title("Blackjack")


class card_class:
    def __init__(self, suits, card) -> None:
        self.suits = suits
        self.card = card

    def get_list(self):
        return [self.suits, self.card]


entry_player = tk.Entry(app, width=50)
entry_player.grid(row=4, column=1)


# create deck
cards = []
list_player = []
suits_list = ["spade", "spade_2", "club", "club_2",
              "diamond", "diamond_2", "heart", "heart_2"]


def create_deck():
    global suits
    for suits in suits_list:
        for card in range(1, 11):
            card1 = card_class(suits, card).get_list()
            cards.append(card1)
    return cards


def pick_card():
    card = random.choice(cards)
    return card


# pick cards
x = 0


def start_game():
    global x
    x = int(entry_player.get())
    for i in range(1, x+1):
        list_player.append(i)
    for player in list_player:
        print("Player: " + str(player))
        played_card_1 = pick_card()
        played_card_2 = pick_card()
        global played_card_list
        played_card_list = played_card_1 + played_card_2
        add_card_to_player_hand(player, played_card_list)
    # pick_card_dealer()
    # pick_second_dealer_card()


player_hand = []


def add_card_to_player_hand(player, played_card_list):

    player_hand = globals()[
        f"player_hand{player}"] = played_card_list
    print(player_hand)
    print(parse_integers(played_card_list))


def pick_card_after_start():
    global x
    if k < x+1:
        globals()[f"player_hand{k}"].extend(pick_card())
        print("This is a test2 " + str(globals()[f"player_hand{k}"]))
        print(globals()[f"player_hand{k}"])
        print(parse_integers(globals()[f"player_hand{k}"]))
        k += k


def set_k_value():
    pick_card_after_start(1)


def parse_integers(parse_integers_played_card_list):
    new_list = [i for i in parse_integers_played_card_list if type(i) == int]
    count_cards(new_list)
    return new_list


# dealer card picking
def pick_card_dealer():
    card = random.choice(cards)
    print("Dealer Card: " + str(card))


def pick_second_dealer_card():
    hidden_card = random.choice(cards)
    print("Hidden Dealer Card")
    return hidden_card


def check_and_schuffle():
    if len(cards) < 18:
        cards.clear()
        create_deck()
    else:
        pass


# counting card value
def count_cards(list_values):
    hand_value = sum(list_values)
    print("Your Hand_value is: " + str(hand_value))
    check_hand_value(hand_value)

# checking card value


def check_hand_value(checking_hand_value):
    if checking_hand_value < 22:
        pass
    elif checking_hand_value == 21:
        print("You won")
    elif checking_hand_value > 21:
        print("You lost")


create_deck()


pick_card_btn = tk.Button(app, text="start_game", command=start_game)
pick_card_btn.grid(row=0, column=1)
pick_card_btn = tk.Button(app, text="pick_card",
                          command=pick_card_after_start)
pick_card_btn.grid(row=1, column=1)
stay_btn = tk.Button(app, text="stay",
                     command=set_k_value)
stay_btn.grid(row=2, column=1)
# pick_card_btn = tk.Button(app, text="create deck", command=create_deck)
# pick_card_btn.grid(row=1,column=1)

app.mainloop()
