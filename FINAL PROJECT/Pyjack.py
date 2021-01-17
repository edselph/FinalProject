#  This is blackjack 21
# Ace is 1/11
# JQK = 10
# Dealer can only have 2 card

import random as RD

# Class for card, suit and value
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    # calling it self for the suit and value of card

    def __repr__(self):
        return " of ".join((self.value, self.suit))
        # when printing will have the value "of suit"

# inside the card deck 
class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in ["Spades", "Clover",
         "Hearts", "Diamonds"] for v in
                      ["A", "2", "3", "4", "5", "6",
                       "7", "8", "9", "10", "J", "Q", "K"]]
                    #    making the card to have suit (the symbol), and to have the value 1-k

    def shuffle(self):
        if len(self.cards) > 1:
            RD.shuffle(self.cards)
            # for shuffling the card suit and value

    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0) 
            # delet card that have been taken

# you the player hand and the dealer hand
class Hand:
    def __init__(self, dealer=False):
        self.dealer = dealer
        self.cards = []
        # empty list
        self.value = 0
        # calling it self

    def add_card(self, card):
        self.cards.append(card)
        # adding card and minus the card form the deck

    def Calcu_Value(self):
        # this is for calculating the value of the card
        self.value = 0
        has_ace = False
        for card in self.cards:
            if card.value.isnumeric():
                self.value += int(card.value)
            else:
                if card.value == "A":
                    has_ace = True
                    self.value += 11
                    # this is making the value ace to be 11
                else:
                    self.value += 10
                # this is for J,Q, AND K to be automatically 10 
        if has_ace and self.value > 21:
            self.value -= 10
            #making the value ace to be 1 if the value of the card is over 21   

    def get_value(self):
        self.Calcu_Value()
        return self.value
        # this is for calling the value

    def display(self):
        if self.dealer:
            print("hidden")
            print(self.cards[0])
            # displaying hidden card for the dealer 
        else:
            for card in self.cards:
                print(card)
            print("Value:", self.get_value())
            # only displaying 1 value card for dealer

# the meat of the code
class Game:
    def play(self):
        playing = True
        # starting the game
        while playing:
            self.deck = Deck()
            # calling the deck class
            self.deck.shuffle()
            # shuffling deck

            self.player_hand = Hand()
            # calling the hand class for player
            self.dealer_hand = Hand(dealer=True)
            # calling the hand class for dealer

            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())
            # this is to start the code 

            print("Your hand is:")
            self.player_hand.display()
            print("Dealer's hand is:")
            self.dealer_hand.display()
            # for printing the hand of player and the hand for dealer

            game_over = False
            # to end game
            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                # this is for checking for blackjack in the hand of player and dealer
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    # ending the game with a win
                    self.show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
                    continue

                choice = input("Please choose [Hit / stay] ").lower()
                # input the hit or stay, the awnser will always be lower case
                while choice not in ["h", "s", "hit", "stay"]:
                    choice = input("Please enter 'hit' or 'stay' (or H/S) ").lower()
                    # this is to make a choise for hit or stay, and it's on loop
                if choice in ['hit', 'h']:
                    # choice if player choose h/hit
                    self.player_hand.add_card(self.deck.deal())
                    # this is for adding the card
                    self.player_hand.display()
                    if self.player_is_over():
                        # to check the value on card not over 21
                        print("You have lost!")
                        # game over card value over 21
                        game_over = True
                else:
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()
                    # calculating the value for player and dealer
                    print("Final Results")
                    print("Your hand:", player_hand_value)
                    print("Dealer's hand:", dealer_hand_value)
                    # printing the final result
                    if player_hand_value > dealer_hand_value:
                        # if palyer have more value than dealer, player win
                        print("You Win!")
                    elif player_hand_value == dealer_hand_value:
                        # making draw because dealer and player have 21
                        print("Tie!")
                    else:
                        # dealer win because have more card
                        print("Dealer Wins!")
                    game_over = True
            
            again = input("Play Again? [Y/N] ")
            while again.lower() not in ["y", "n"]:
                # making loop to start or end game
                again = input("Please enter Y or N ")
            if again.lower() == "n":
                print("Thanks for playing")
                playing = False
            else:
                game_over = False

    def player_is_over(self):
        return self.player_hand.get_value() > 21
        # checking the value card for player over 21

    def check_for_blackjack(self):
        # this is for checking to playr or the dealer have a 21
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            # checking the value for player to check the value is 21
            player = True
        if self.dealer_hand.get_value() == 21:
            # checking the value for dealer to check the value is 21
            dealer = True

        return player, dealer

    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack! Draw")
            # both have blackjack a draw
        elif player_has_blackjack:
            print("You have blackjack! You win")
            # player have blackjack
        elif dealer_has_blackjack:
            print("Dealer has blackjack! Dealer wins")
            # dealer have blackjack

    def dealer_hit(self):
        if self.dealer_hand.get_value < 15 :
            self.dealer_hand.add_card.append(self.deck.deal.pop(0))
            dealer_hand.get_value.display
            # if dealer have lower than 15 of value, dealer draw card



g = Game()
g.play()
# start game
