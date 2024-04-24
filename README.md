# Colin's Card Memory Game

This code c

## Installation

t

## License

#need to shuffle my deck so its random!
def shuffle():
    #.shuffle is inbuilt module in random that will randomly reorder my deck
    random.shuffle(deck)
    # Initialize a hand for the player
    player_hand = []
    # Deal 5 cards to the player
    for _ in range(5):
        deal_card(deck, player_hand)
    # Print the player's hand
    print("Player's hand:", player_hand)

shuffle(deck)