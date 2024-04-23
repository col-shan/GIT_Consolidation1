#creating a card game based on memorization between two players
#there will be 5 rounds (best of 5), 1 round requires both players go
#must create values for my deck of 52 cards first
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

#need to randomize the cards
import random

#shuffle (looked it up) is inbuilt module in random that will randomly reorder the deck list I created
random.shuffle(deck)
print(deck)

card = random.choice(deck)
print(card)
#used choice module in random this time to deal a random card, but keeps giving me the same card. must find way for it to remove said card
    #out of deck of 52 and deal a different card from remaining 51 left
#.pop will remove a card from the deck for the rest of the game and also assign it to my player so he can memorize it
