'''Debugging Coin Toss
The following program is meant to be a simple coin toss guessing game. The player gets two guesses (it’s an easy game). However, the program has several bugs in it. Run through the program a few times to find the bugs that keep the program from working correctly.
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
'''
from details import details
details()
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()  
toss = random.randint(0, 1)
if (toss == 1 and guess == 'heads') or (toss == 0 and guess == 'tails'):
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input().lower()
    if (toss == 1 and guess == 'heads') or (toss == 0 and guess == 'tails'):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
