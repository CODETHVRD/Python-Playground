
 
#Try to limit the number of goes a player can have before the game ends.

#If the game ends, ask them if they want to play again, if they say yes, then restart the game play automatically.

import random
number = random.randint(1,10)
is_Guess_Correct = False
guess_counter = 0
guesses_allowed = 6

while is_Guess_Correct is not True:
    guess = input('Guess a number between 1 and 10: ')
    if int(guess) not in range(1,10):
        print('Please enter a valid number between 1 and 10')
    else:
        if int(guess) == number:
            print(f'You guessed {guess}. That is correct! You win!')
            isGuessRight = True
            break
        else:
            print(f'You guessed {guess}. Sorry, that isn’t it. Try again.')
            guess_counter +=1
            while guess_counter != guesses_allowed:
                guesses_allowed -= 1
                guess = (f'You have {guesses_allowed} guesses left')
                if guess_counter == guesses_allowed :
                    print ('\nYou have reached the number of guesses allowed')
                    break
            