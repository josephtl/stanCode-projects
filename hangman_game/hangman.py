"""
File: hangman.py
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
to try in order to win this game.
"""


import random


# This constant controls the number of guess the player has
N_TURNS = 7


def main():
    """
    This program present the classic hangman game.
    At the beginning, it will randomly show a string of blanks to let users to guess.
    Users need to guess one alphabet at a time, and also try to complete it before running out of turns.
    """
    r = random_word()
    status = ''
    for i in range(len(r)):
        status += '_'
    print('The word looks like: ' + str(status))
    print('\nYou have ' + str(N_TURNS) + ' guesses left.')
    guessing(r, status)


def random_word():
    """
    It will randomly return a word among those 9 below.
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def guessing(r, status):
    """
    :param r: str, random word to be guess
    :param status: str, the blanks presenting the number of letters of the random word
    :return: str, it might show either one of five conditions,
    illegal format, wrong guesses, right guesses, you win and you lose.
    """
    turns = N_TURNS
    while True:
        guess = str(input('Your guess: '))
        guess = guess.upper()

        # illegal format, ex. more than one alphabet or not an alphabet
        if not guess.isalpha() or len(guess) > 1:
            print('illegal format.')
        # wrong guesses
        elif r.find(guess) == -1:
            print('There is no ' + str(guess) + '\'s in the word.')
            if turns > 1:
                print('The word looks like: ' + str(status))
                # losing one turn
                turns -= 1
                print('You have ' + str(turns) + ' guesses left.')
            # losing the game
            else:
                print('You are completely hung :(')
                print('The word was: ' + str(r))
                break
        # right guesses
        else:
            new = ''
            for i in range(len(r)):
                if r[i] == guess:
                    new += guess
                else:
                    new += status[i]
            status = new
            print('You are correct!')

            # win the game, means all blanks turn into alphabets.
            if status.isalpha():
                print('You win!!')
                print('The word was: ' + str(status))
                break
            # right guesses and keep going, also keep the turn.
            else:
                print('The word looks like: ' + str(status))
                print('You have ' + str(turns) + ' guesses left.')


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
