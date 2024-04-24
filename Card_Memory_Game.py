#creating a card game based on memorization
#there will be 5 rounds (best of 5)
#the player will score points by remembering specific aspects of cards that they were shown
#the cards will only show for 2 seconds at a time

#import file paths
import os
#import so I can randomize the cards
import random

#must create function with 52 values for my deck
#will use tuples, with cards as ints and suits as strings
def create_deck():
    #create my 2 lists consisting of suits and ranks
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    #range must add 1, so because i want 2 through 10 i must do 2-11 as 11 isn't included! that took a while to figure out lol
    ranks = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    #now loop my lists together in every rank and suit combination to my tuples of every possible card combination
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

#have now created a list of tuples to create my deck! time to print it
deck = create_deck()
print(deck)

random.shuffle(deck)

#must now simulate what a dealer does by moving one card from my deck to a players hand
#create my arguments for both my deck of cards, and the hand of the player
def deal_card(deck, hand):
    #used pop to permanently remove card from my deck (no repeating cards)
    card = deck.pop()
    #use append to assign card to the players hand
    hand.append(card)

#create my player's empty hand
player_hand = []

#deal a card to the player's hand
deal_card(deck, player_hand)

#print out what card the player got
print("Player's Hand:", player_hand)