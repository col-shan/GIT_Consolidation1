#creating a card game based on memorization
#each card in my deck will contain the typical suits and ranks values
#the dealer will flip 4 cards at a time, with each one displayed for only 2 seconds
#there will be 5 rounds
#the player will score points by remembering specific aspects of cards that they were shown

#import file paths
import os
#import so I can randomize the cards and suit or ranks the player needs to guess
import random
#import so I can set time limit on how long each card is shown for
import time
#import the deck of cards I created
import deck

my_deck = deck.create_deck()
#use inbuilt shuffle module in random to shuffle my deck (randomize card dealt)
random.shuffle(my_deck)

#must now simulate what a dealer does by moving one card from my deck to a players hand
#create my arguments for both my deck of cards, and the hand of the player
def deal_card(my_deck, hand):
    #used pop to permanently remove card from my deck (no repeating cards)
    card = my_deck.pop()
    #use append to assign card to the players hand
    hand.append(card)

#create my player's empty hand
player_hand = []

#deal 4 cards to the player's hand
for _ in range(4):
    deal_card(my_deck, player_hand)
    #print out the 4 cards indivually instead of all grouped together
    for card in player_hand:
        rank, suit = card
    #print out what card the player got
    print("You drew:", rank, "of", suit)
    #show cards for 2 seconds (looked up how to do this and screen clear via StackOverflow)
    time.sleep(2)
    #dealer must take back cards after they are dealt (memorization aspect, cards must disappear(clears the terminal screen))
    os.system('cls' if os.name == 'nt' else 'clear')

#dealer randomly selects suits or ranks for player to guess
suits_or_ranks = random.choice(["Suits", "Ranks"])
print("You need to guess the ", suits_or_ranks)

#player must list out suits or ranks depending on the dealer's random choice
if suits_or_ranks == "Suits":
    player_guess = input("List the suits (Hearts, Diamonds, Clubs, Ace) of the cards that were dealt: ")
else:
    player_guess = input("List the ranks (2 through 10 or Jack/Queen/King/Ace) of the cards that were dealt: ")
