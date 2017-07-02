# this is a guess the number game
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# ask the player to guess 6 times.
for guessTaken in range(1, 7):
    print('take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('your guess is low.')
    elif guess > secretNumber:
        print('your guess is high.')
    else:
        break   # this condition is correct.

if guess == secretNumber:
    print('good job! you guessed my number in ' + str(guessTaken) +' guesses!')
else:
    print('nope the number i was thinking of ' + str(secretNumber))
