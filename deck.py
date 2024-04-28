#must create function with 52 values for my deck
#will use tuples, with cards as ints and suits as strings
def create_deck():
    #create my 2 lists consisting of suits and ranks
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    #range must add 1, so because i want 2 through 10 i must do 2-11 as 11 isn't included! that took a while to figure out lol
    ranks = list(range(2, 11)) + ['jack', 'queen', 'king', 'ace']
    #now loop my lists together in every rank and suit combination to my tuples of every possible card combination
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

#will now impport this module containing my deck of cards into my main code