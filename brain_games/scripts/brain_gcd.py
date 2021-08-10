#!/usr/bin/env python

import random
from brain_games.cli import welcome_user
import math


def game_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    count = 1
    answer = ''
    divisor = ''

    while count <= 3:
        count += 1
        number1, number2 = random.randint(1, 100), random.randint(1, 100)
        given_numbers = str(number1) + ' ' + str(number2)
        print('Question: ' + str(given_numbers))
        answer = input('Your answer: ')
        divisor = math.gcd(number1, number2)

        if answer == str(divisor):
            print('Correct!')
        else:
            print(("'" + str(answer) + "' is wrong answer ;(. "
                   "Correct answer was'" + str(divisor) + "'. \nLet's "
                   "try again, " + name + "!"))
    if count > 3 and answer == str(divisor):
        print('Congratulations, ' + name + '!')
