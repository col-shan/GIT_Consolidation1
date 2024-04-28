#import file paths
import os
#import so I can randomize the cards and suit or ranks the player needs to guess
import random
#import so I can set time limit on how long each card is shown for
import time
#import the deck of cards I created
import deck

#simulate what a dealer does by moving one card from my deck to the players hand
#create my arguments for both my deck of cards, and hand of the player
def deal_card(my_deck, hand):
    #used pop to remove the card from my deck (no repeating cards)
    card = my_deck.pop()
    #used append to add the card to the players hand
    hand.append(card)

#talk to the player and let them know what's going on!!
print("Welcome to Colin's Card Memorization Game! You are about to be shown 4 cards, one at a time for 2.5 seconds each.")
print("Your goal is to memorize the suits and ranks of each card in the order of which they were dealt.")
print("One point will be awarded for every correct answer you get, and there will be 5 rounds. Let's begin!")

#put everything else into one big function to create my rounds
def play_round():
    my_deck = deck.create_deck()
    #use inbuilt shuffle module in random to shuffle my deck (randomize card dealt)
    random.shuffle(my_deck)
    #test case 1 below: print out shuffled deck of cards
    #print(my_deck)

    #create the player's empty hand
    player_hand = []
    #create the player's score
    score = 0

    #deal 4 cards to the player's hand
    for _ in range(4):
        deal_card(my_deck, player_hand)
        #print out the 4 cards indivually instead of all grouped together
        for card in player_hand[-1:]:
            #unpack my tupled deck of cards
            rank, suit = card
            #print out what card the player got
            print("You drew:", rank, "of", suit)
            #show each card for 2 and a half seconds
            time.sleep(2.5)
            #dealer must take back cards after they're dealt
            #memorization aspect, cards must disappear(looked up how to clear terminal screen via StackOverflow)
            os.system('cls' if os.name == 'nt' else 'clear')

    #continue guiding player through the game
    print("Time to test your recall! The dealer will now pick either the suits or ranks of the cards that were dealt.")
    print("You must list out the corresponding values, using commas to separate your answers. It should look like this: 8, 10, king, 2")
    
    #dealer randomly selects suits or ranks for player to guess
    suits_or_ranks = random.choice(["Suits", "Ranks"])
    #test case 2 below: tells the player which value they must try to recite
    #print("You need to guess the", suits_or_ranks)

    #player must list out suits or ranks depending on the dealer's random choice
    if suits_or_ranks == "Suits":
        #have player input their guesses for suit
        player_guess = input("The dealer has picked suits (hearts, diamonds, clubs, spades)! Type them in order please: ")
    else:
        #have player input their guesses for rank
        player_guess = input("The dealer has picked ranks (2 through 10 or jack/queen/king/ace)! Type them in order please: ")

    #player's guesses are split into a list so that all 4 can be read
    player_guesses = player_guess.split(", ")

    #create a loop to iterate over the four cards the player was briefly shown
    for i in range(len(player_hand)):
        #use try/except block to match up dealt cards with guesses and account for if the player doesn't provide 4 guesses
        try:
            guess = player_guesses[i]
        #if not enough guesses were made, let the player know and score accordingly
        except IndexError:
            print("You failed to provide a guess for this card :(")
            continue
        #if dealer chose suits
        if suits_or_ranks == "Suits":
            #check if guess matches the suit of current card, and print and score accordingly with if/else for either scenario
            if guess == player_hand[i][1]:
                print(f"You guessed correctly, the suit was {player_hand[i][1]}!")
                score += 1
            else:
                print(f"Ah you got this one wrong, the right suit was {player_hand[i][1]}.")
        #if dealer chose ranks
        else:  
            #convert all numbers in my ranks (2-10) into strings so that program can properly score it (needed lots of online help here)
            card_rank = str(player_hand[i][0]) if isinstance(player_hand[i][0], int) else player_hand[i][0]
            #check if guess matches the rank of current card, and print and score accordingly with if/else for either scenario
            if guess == card_rank:
                print(f"You guessed correctly, the rank was {card_rank}!")
                score += 1
            else:
                print(f"Ah you got this one wrong, the right rank was {card_rank}.")

    #show player's score for the round
    print(f"Your score for this round is: {score}.")
    return score

total_score = 0
#loop my rounds function 5 times
for round_number in range(1, 6):
    #show player what round they are in
    print(f"Round {round_number} of 5!")
    #call my play_round function and have it remember the player's score for it
    round_score = play_round()
    #add the player's score from their current round to the score obtained from every round before to keep adding onto the total score
    total_score += round_score
    #6 second delay between rounds for player to see score and what they got right or wrong
    time.sleep(6)

#send the player off!!
print(f"Your total score for all 5 rounds is: {total_score}! Congratulations, and please come back to play again later to try and beat it.")