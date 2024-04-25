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

#create the player's empty hand
player_hand = []
#create the player's score
score = 0
print("Your starting score is: 0, lets see how high you can get in 5 turns!")

#deal 4 cards to the player's hand
for _ in range(4):
    deal_card(my_deck, player_hand)
    #print out the 4 cards indivually instead of all grouped together
    for card in player_hand:
        rank, suit = card
        #print out what card the player got
        print("You drew:", rank, "of", suit)
        #show cards for 2 seconds
        time.sleep(2)
        #dealer must take back cards after they're dealt
        #memorization aspect, cards must disappear(looked up how to clear terminal screen via StackOverflow)
        os.system('cls' if os.name == 'nt' else 'clear')

#dealer randomly selects suits or ranks for player to guess
suits_or_ranks = random.choice(["Suits", "Ranks"])
#tells the player which value they must try to recite
print("You need to guess the", suits_or_ranks)

#player must list out suits or ranks depending on the dealer's random choice
if suits_or_ranks == "Suits":
    player_guess = input("List the suits (Hearts, Diamonds, Clubs, Ace) of the cards that were dealt: ")
else:
    player_guess = input("List the ranks (2 through 10 or Jack/Queen/King/Ace) of the cards that were dealt: ")

# Split player's input into a list of guesses
player_guesses = player_guess.split(", ")

# Check each card in the player's hand
for card in player_hand:
    # Check if the guess matches the appropriate attribute (suit or rank) of the card
    if suits_or_ranks == "Suits":
        # If the guessed suit matches the card's suit, award 1 point
        if card[1] in player_guesses:
            print(f"Correct guess: {card[1]}")
            score += 1
        else:
            print(f"Incorrect guess: {card[1]}")
            score -= 1
    else:  # If the dealer chose "Ranks"
        if card[0] in player_guesses:
            print(f"Correct guess: {card[0]}")
            score += 1
        else:
            print(f"Incorrect guess: {card[0]}")
            score -= 1

# Display player's final score
print(f"Your final score is: {score}")