#Program 3
#CIS 443-75
#Due: 3-28-2021
#Grading ID: P5696
#This simulates a game of craps and organizes the output of 1 million games by the total rolls taken to win/lose

# fig04_02.py
"""Simulating the dice game Craps."""
import random

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

def display_dice(dice):
    """Display one roll of the two dice."""
    die1, die2 = dice  # unpack the tuple into variables die1 and die2
    #print(f'Player rolled {die1} + {die2} = {sum(dice)}')

def game_craps(total_games):
    wins = {}
    losses = {}
    game = 0     #Determines which game we are on
    while game != total_games:
        rolls = 0 #Rolls taken to resolve game
        die_values = roll_dice()  # first roll
        display_dice(die_values)
        rolls += 1
        # determine game status and point, based on first roll
        sum_of_dice = sum(die_values)
  
        if sum_of_dice in (7, 11):  # win
            game_status = 'WON'
            if rolls in wins:
                wins[rolls] += 1
            else:
                wins[rolls] = 1
        elif sum_of_dice in (2, 3, 12):  # lose
            game_status = 'LOST'
            if rolls in losses:
                losses[rolls] += 1
            else:
                    losses[rolls] = 1
        else:  # remember point
            game_status = 'CONTINUE'
            my_point = sum_of_dice
            #print('Point is', my_point)
   
        # continue rolling until player wins or loses
        while game_status == 'CONTINUE':
            die_values = roll_dice()
            rolls += 1
            display_dice(die_values)
            sum_of_dice = sum(die_values)
            if sum_of_dice == my_point:  # win by making point
                game_status = 'WON'
                if rolls in wins:
                    wins[rolls] += 1
                else:
                    wins[rolls] = 1
            elif sum_of_dice == 7:  # lose by rolling 7
                game_status = 'LOST'
                if rolls in losses:
                    losses[rolls] += 1
                else:
                    losses[rolls] = 1

        # display "wins" or "loses" message
        #if game_status == 'WON':
            #print('Player wins')
        #else:
            #print('Player loses')
        game += 1
    
    #Output
    print(f"Percentage of Wins: {(sum(wins.values())/total_games)*100:2.2f}%")
    print(f"Percentage of Losses: {(sum(losses.values())/total_games)*100:2.2f}%")
    print()
    print("Percentage of wins/losses based on total number of rolls:")
    print(f"\t\t {'% Resolved':<}\t\t  {'Cumulative %':>}")
    print(f"{'Rolls':<}\t{'on this roll'}\t{'of games resolved':>}")
        
    i = 1
    running_total = 0
    while i != total_games:
        total = 0 #Determines total games resolved with that roll
        if wins.get(i):
            total += wins[i]
        if losses.get(i):
            total += losses[i]
        if total != 0: #Only prints the % if this was a resolved roll
            running_total += total
            print(f"{i:>5}\t {(total/total_games)*100:.2e}% \t\t   {(running_total/total_games)*100:>.2e}%")
        i += 1
    
# ------------------------------------------------------ (separating code)
total_games = 1000000   #Total number of games to be played
game_craps(total_games)
