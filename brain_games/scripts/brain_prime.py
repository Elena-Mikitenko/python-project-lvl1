#!/usr/bin/env python

from random import randint
from brain_games.cli import welcome_user


def game_prime():
    name = welcome_user()
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    count = 1
    answer = ''
    correct_answer = ''
    while count <= 3:
        count += 1
        number = randint(1, 60)

        if number % 2 == 0 and number != 2:
            correct_answer = 'no'
        else:
            correct_answer = 'yes'
        print('Question: ' + str(number))
        answer = input('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            continue
        else:
            print(("'" + answer + "' is wrong answer ;(. "
                   "Correct answer was '" + correct_answer + "'.\nLet's "
                   "try again, " + name + "!"))
            continue
    if count > 3 and answer == correct_answer:
        print('Congratulations, ' + name + '!')
