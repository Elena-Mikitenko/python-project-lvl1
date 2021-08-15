#!/usr/bin/env python

import random
from operator import add, sub, mul

games_purpose = 'What is the result of the expression?'


def game_process():
    random_sign = {'+': add, '-': sub, '*': mul}
    number1, number2 = random.randint(1, 100), random.randint(1, 100)
    sign = list(random_sign.keys())
    my_char = random.choice(sign)
    question = '{} {} {}'.format(number1, my_char, number2)
    answer = str(random_sign[my_char](number1, number2))
    return question, answer
