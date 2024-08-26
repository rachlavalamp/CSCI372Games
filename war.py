################################################################################################
#   Rachel Lavallee
#   War Card Game Simulator
#   This project is a simulator for the card game of War. This game is for a single player to
#   play against a computer player.
################################################################################################

import random
# import pygame
#
# pygame.init()
#
# canvas = pygame.display.set_mode((500, 500))
# pygame.display.set_caption("My Board")
# exit = False
#
# while not exit:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit = True
#     pygame.display.update()

class Card:
    # Initializes a new Card object
    def __init__(self, suit, rank):
        self.suit = suit        # Sets the Card object's suit property
        self.rank = rank        # Sets the Card object's rank property

    def __str__(self):
        return f"{self.rank} of {self.suit}"        # Returns the rank and suit of the Card object


class Deck:

    # Initializes a new Deck object
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = list(range(2, 15))  # 2-10 for numbers, 11-14 for Jack, Queen, King, Ace
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]  # Creates Card objects for Deck
        random.shuffle(self.cards)      # Shuffles all of the cards in the Deck randomly

    def deal_card(self):
        return self.cards.pop()         # Deals the first Card object

    def size(self):
        return len(self.cards)          # Returns the amount of cards in the Deck


class Player:

    # Initializes a new Player object
    def __init__(self, name):
        self.name = name            # Sets the Player's name property
        self.hand = []              # Creates an empty array for the Player's hand property

    def receive_card(self, card):
        self.hand.append(card)      # Receive card if you win the round

    def play_card(self):
        return self.hand.pop(0)     # Take the first card from your pile

    def hand_size(self):
        return len(self.hand)       # Returns the amount of cards in a player's hand

    def __str__(self):
        return self.name            # Returns the player's name


def play_round(player1, player2):
    input("Press enter to play round... ")
    card1 = player1.play_card()                     # Player 1's turn
    card2 = player2.play_card()                     # Player 2's turn

    print(f"{player1} plays: {card1}")
    print(f"{player2} plays: {card2}")

    # Compares players cards to see who wins the round
    if card1.rank > card2.rank:
        player1.receive_card(card1)
        player1.receive_card(card2)
        print(f"{player1} wins the round.\n")
    elif card1.rank < card2.rank:
        player2.receive_card(card1)
        player2.receive_card(card2)
        print(f"{player2} wins the round.\n")
    else:
        print("WAR!")
        handle_war(player1, player2, card1, card2)

def handle_war(player1, player2, war_card1, war_card2):
    war_pile = [war_card1, war_card2]           # Create war piles for user and computer

    # If a player doesn't have enough cards, then they lose!
    if player1.hand_size() < 4 or player2.hand_size() < 4:
        print("One player doesn't have enough cards for war. The game ends.")
        return

    # WAR! Each player deals 3 cards
    for _ in range(3):
        war_pile.append(player1.play_card())
        war_pile.append(player2.play_card())

    war_card1_face_up = player1.play_card()
    war_card2_face_up = player2.play_card()

    print(f"{player1} plays: {war_card1_face_up}")
    print(f"{player2} plays: {war_card2_face_up}")

    # Compares user's and computer's cards
    if war_card1_face_up.rank > war_card2_face_up.rank:
        player1.receive_card(war_card1_face_up)         # User receives card from winning war
        player1.receive_card(war_card2_face_up)         # User receives card from winning war
        print(f"{player1} wins the war.\n")
    elif war_card1_face_up.rank < war_card2_face_up.rank:
        player2.receive_card(war_card1_face_up)         # Computer receives card from winning war
        player2.receive_card(war_card2_face_up)         # Computer receives card from winning war
        print(f"{player2} wins the war.\n")
    else:
        print("The war continues!")
        handle_war(player1, player2, war_card1_face_up, war_card2_face_up)      # War is played again!

    player1.receive_card(war_card1_face_up)         # User receives card from winning war
    player2.receive_card(war_card2_face_up)         # Computer receives card from winning war


# Main function
def main():
    print("Welcome to the War Card Game Simulator!")
    # num_players = int("Enter number of players: ")
    #
    # players = [];
    # for i in range(num_players):
    #     player_name = input(f"Enter Player {i + 1}'s name: ")
    #     players.append(Player(player_name))

    player_name = input("Enter your name: ")

    user = Player(player_name)              # Creates Player object for user
    computer = Player("Computer")           # Creates Player object for computer
    deck = Deck()                           # Creates a Deck object

    # Deal cards evenly to players
    while deck.size() > 0:
        user.receive_card(deck.deal_card())         # User receives a deck of shuffled cards
        computer.receive_card(deck.deal_card())     # Computer receives a deck of shuffled cards

    # Keep playing rounds until either the user or the computer has zero cards
    while user.hand_size() > 0 and computer.hand_size() > 0:
        play_round(user, computer)          # Play a round between the user and computer

    # Print statements for who wins the game
    if user.hand_size() > 0:
        print(f"Congrats {user}, you win the game!")
    else:
        print(f"{computer} wins the game!")


if __name__ == "__main__":
    main()

