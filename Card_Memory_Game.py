#import file paths
import os
#import so I can randomize the cards and suit or ranks the player needs to guess
import random
#import so I can set time limit on how long each card is shown for
import time
#import the deck of cards I created
import deck
#import the graphing software I need and abbreviate it to just plt
import matplotlib.pyplot as plt

def deal_card(my_deck, hand):
    """
    The purpose of this function is to simulate what a dealer would do by creating arguments for both the deck of cards I 
    created and imported and the hand of the player. When "dealt", the card will be simultaneously added to the player's hand
    and removed from the existing deck so that no cards will repeat.
    """
    #used pop to remove the card from my deck (no repeating cards)
    card = my_deck.pop()
    #used append to add the card to the players hand
    hand.append(card)

def display_high_score():
    """
    The purpose of this function is to read in all of the values found in my high_score text file and then find the highest value/
    score among them and print it out so that the player will know the high score for them to beat.
    """
    #open my file in read mode
    with open("high_score.txt", "r") as file:
        #read all lines from my file
        high_scores = file.readlines()
        #convert every line from my file to an integer
        high_scores = [int(score.strip()) for score in high_scores]
        #get the highest score from my file
        highest_score = max(high_scores)
        #return the highest existing score so far! will then print it with rest of my printed directions
        return highest_score

def update_score(score):
    """
    The purpose of this function is to write in whatever value/score the player ended up with from their current game into my high_score
    text file so that every score ever received by a player is documented and can be accessed to create cool data plots.
    """
    #open my file and allow to append it
    with open("high_score.txt", "a") as file:
        #write in player's score
        file.write(str(score) + "\n")


def play_round():
    """
    The purpose of this function is to create the rounds of my game, which I will iterate over later in the code. It's responsible for 
    calling and shuffling my imported deck, dealing 4 cards to the player one at a time, having the dealer ranomly decide either suits
    or ranks, and then having the player input their 4 guess and correctly scoring them depending on whether they were right or wrong.
    All the while there are printed messages throughout to guide the player on what to next!
    """
    #create variable to recalled my imported deck with
    my_deck = deck.create_deck()
    #use inbuilt shuffle module in random to shuffle my deck (randomize card dealt)
    random.shuffle(my_deck)
    #test case 1 below: print out shuffled deck of cards
    #print(my_deck)

    #create the player's empty hand
    player_hand = []
    #initialize the player's score
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
            #memorization aspect, cards must disappear (looked up how to clear terminal screen via StackOverflow)
            os.system('cls' if os.name == 'nt' else 'clear')

    #continue guiding player through the game
    print("Time to test your recall! The dealer will now pick either the suits or ranks of the cards that were dealt.")
    print("You must list out the corresponding values, using commas to separate your answers. It should look like this: ?, ?, ?, ?")
    
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
        #if not enough guesses were made, let the player know and score accordingly (online help to use IndexError as a specific exception)
        except IndexError:
            print("You didn't make a guess for this card :(")
            #keep my program going even if they didn't make a guess so the player can finish the game
            continue
        #if dealer chose suits
        if suits_or_ranks == "Suits":
            #use f-string to access the player's hand at index of 1 (which is suits)
            #check if guess matches the suit of current card, and print and score accordingly with if/else for either scenario
            if guess == player_hand[i][1]:
                print(f"You guessed correctly, the suit was {player_hand[i][1]}!")
                #give player a point for every correct guess of the rank they made
                score += 1
            #if player was wrong, don't give them a point and print to let them know what the correct guess would've been
            else:
                print(f"Ah you got this one wrong, the right suit was {player_hand[i][1]}.")
        #if dealer chose ranks
        else:  
            #use f-string to access the player's hand at index of 0 (which is ranks)
            #convert all numbers in my ranks (2-10) into strings so that program can properly score it (needed lots of online help here)
            card_rank = str(player_hand[i][0]) if isinstance(player_hand[i][0], int) else player_hand[i][0]
            #check if guess matches the rank of current card, and print and score accordingly with if/else for either scenario
            if guess == card_rank:
                print(f"You guessed correctly, the rank was {card_rank}!")
                #give player a point for every correct guess of the rank they made
                score += 1
            #if player was wrong, don't give them a point and print to let them know what the correct guess would've been
            else:
                print(f"Ah you got this one wrong, the right rank was {card_rank}.")

    #show player's score for the round
    print(f"Your score for this round is: {score}.")
    return score

#clear terminal screen so player knows game is beginning and focuses (looked up how to clear terminal screen via StackOverflow)
os.system('cls' if os.name == 'nt' else 'clear')
#talk to the player and let them know what's going on!!
print("Welcome to Colin's Card Memorization Game! You are about to be shown 4 cards, one at a time for 2.5 seconds each.")
print("Your goal is to memorize the suits and ranks of each card in the order of which they were dealt.")
print("One point will be awarded for every correct answer you get, and there will be 5 rounds.")
#recall my display_high_score function from above and it's returned output
highest_score = display_high_score()
#print existing high score
print(f"The highest score achieved so far is: {highest_score}. Lets begin!")
#give player 10 seconds to read my instructions the cards are dealt (and screen is wiped)
time.sleep(10)

#initizialize the player's end score
total_score = 0
#crux of my program right here! this for loop will iterate over my play_round function 5 times to create 5 different turns
for round_number in range(1, 6):
    #show player what round they are in
    print(f"Round {round_number} of 5!")
    #call my play_round function and have it remember the player's score
    round_score = play_round()
    #add the player's score from their current round to the score obtained from every round before to keep adding onto the total score
    total_score += round_score
    #6 second delay between rounds for player to see score and what they got right or wrong
    time.sleep(6)

#clear terminal screen so player can easily discern their score (looked up how to clear terminal screen via StackOverflow)
os.system('cls' if os.name == 'nt' else 'clear')
#put player's score into high score leaderboard
update_score(total_score)
#send the player off with the score they achieved!
print(f"Your total score for all 5 rounds is: {total_score}! Congratulations, and come back to play again later!!")

#time to plot all of the previous scores and the recent user score
def plot_high_scores():
    """
    The purpose of this function is to take all of the previous scores accomplished by players (found in my high_score text file) 
    and convert them into a plot graph once the game is over.
    """
    #open my file in read mode
    with open("high_score.txt", "r") as file:
        #read all lines from my file
        high_scores = file.readlines()
        #convert every line from my file to an integer
        high_scores = [int(score.strip()) for score in high_scores]
    #used online resources to add more detail to my plot than was gone over in lecture
    #plug-in previously created plt to use matplotlib and create my plot graph
    plt.plot(high_scores)
    #give my plot a title
    plt.title('High Scores Over Time')
    #give my plot label for x-axis
    plt.xlabel('Attempt Number')
    #give my plot label for x-axis
    plt.ylabel('Score')
    #create my plot graph
    plt.show()
#display my plot graph!
plot_high_scores()