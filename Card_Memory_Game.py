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
#test code below: print out shuffled deck of cards
#print(my_deck)

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
#talk to the player and let them know what's going on!!
print("Welcome to Colin's Card Memorization Game! You are about to be shown 4 cards, one at a time for 2 seconds each.")
print("Your goal is to memorize the suits and ranks of each card in the order of which they were dealt.")
print("One point will be awarded for every correct answer you get, and there will be 5 rounds. Let's begin!")

#deal 4 cards to the player's hand
for _ in range(4):
    deal_card(my_deck, player_hand)
    #print out the 4 cards indivually instead of all grouped together
    for card in player_hand[-1:]:
        #unpack my tupled deck of cards
        rank, suit = card
        #print out what card the player got
        print("You drew:", rank, "of", suit)
        #show cards for 2 seconds
        time.sleep(2)
        #dealer must take back cards after they're dealt
        #memorization aspect, cards must disappear(looked up how to clear terminal screen via StackOverflow)
        os.system('cls' if os.name == 'nt' else 'clear')

#continue guiding player through the game
print("Time to test your recall! The dealer will now pick either the suits or ranks of the cards that were dealt.")
print("You must list out the corresponding values, using commas to separate your answers. It should look like this: '8, 10, king, 2'")
    
#dealer randomly selects suits or ranks for player to guess
suits_or_ranks = random.choice(["Suits", "Ranks"])
#test code below: tells the player which value they must try to recite
#print("You need to guess the", suits_or_ranks)

#player must list out suits or ranks depending on the dealer's random choice
if suits_or_ranks == "Suits":
    #have user input their guesses for the suit
    player_guess = input("The dealer has picked suits (hearts, diamonds, clubs, spades)! Type them in order please: ")
else:
    #maybe input is problem here? as some values are numeric and others are not
    player_guess = input("The dealer has picked ranks (2 through 10 or jack/queen/king/ace)! Type them in order please: ")

#player's guesses are split into a list so that all 4 can be read
player_guesses = player_guess.split(", ")

#create a loop to iterate over the four cards the player was briefly shown
for i in range(len(player_hand)):
    #create try/except block to match up the correct order of card dealt and the player's guess
    try:
        guess = player_guesses[i]
    #if not enough guesses were made, let the player know and score accordingly
    except IndexError:
        print("No guess provided for this card")
        continue
    #if dealer chose suits
    if suits_or_ranks == "Suits":
        #check if guess matches the suit of current card, and print and score accordingly with if/else for either scenario
        if guess == player_hand[i][1]:
            print(f"Correct guess: {player_hand[i][1]}")
            score += 1
        else:
            print(f"Incorrect guess: {player_hand[i][1]}")
    #if dealer chose ranks
    else:  
        #convert all numbers in my ranks (2-10) into strings so that program can properly score it (needed lots of online help here)
        card_rank = str(player_hand[i][0]) if isinstance(player_hand[i][0], int) else player_hand[i][0]
        #check if guess matches the rank of current card, and print and score accordingly with if/else for either scenario
        if guess == card_rank:
            print(f"Correct guess: {card_rank}")
            score += 1
        else:
            print(f"Incorrect guess: {card_rank}")

print(f"Your final score is: {score}")