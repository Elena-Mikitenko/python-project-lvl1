#!/usr/bin/env python

import math
from random import randint

games_purpose = 'Find the greatest common divisor of given numbers.'


def game_process():
    number1, number2 = randint(1, 100), randint(1, 100)
    question = '{} {}'.format(number1, number2)
    answer = str(math.gcd(number1, number2))
    return question, answer
