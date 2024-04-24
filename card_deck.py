#Deck of Cards

#import so I can randomize the cards
import random


#will use tuples, with cards as ints and suits as strings to create the 52 values for my deck
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

#create my arguments for both my deck of cards, and the hand of my player
def deal_card(deck, hand):
    #used pop to permanently remove card from my deck (no repeating cards)
    card = deck.pop()
    #use append to assign card to the players hand
    hand.append(card)

def main():
    deck = create_deck()
    random.shuffle(deck)


#will now impport my this module containing my deck of cards into my primary code