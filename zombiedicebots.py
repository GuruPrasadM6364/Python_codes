'''write a program to create a bot for the game Zombie Dice
    The bot should be able to play the game and make decisions based on the rules of the game. '''
import random as ran
import time
dice={
    'green':{
        'brain':3,
        'shotgun':1,
        'footprint':2
    },
    'yellow':{
        'brain':2,
        'shotgun':2,
        'footprint':2
    },
    'red':{
        'brain':1,
        'shotgun':3,
        'footprint':2
    }
}
cup=['green','green','green','green','green','green','yellow','yellow','yellow','yellow','red','red','red']
def roll(colour):
    result = []
    for die in colour:
        result.append(ran.choice(list(dice[die].keys())))
    return result
def count_results(results):
    count = {
        'brain': 0,
        'shotgun': 0,
        'footprint': 0
    }
    for result in results:
        count[result] += 1
    return count
def play_game():
    score = 0
    while True:
        print("Rolling colour...")
        results = roll(cup)
        print("Results:", results)
        count = count_results(results)
        print("Count:", count)
        if count['shotgun'] >= 3:
            print("You got shotguns! Game over.")
            break
        score += count['brain']
        print("Current score:", score)
        if input("Do you want to roll again? (y/n)") != 'y':
            break
    print("Final score:", score)
play_game()