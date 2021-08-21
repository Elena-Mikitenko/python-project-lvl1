#!/usr/bin/env python

import random
from operator import add, sub, mul

GAMES_PURPOSE = 'What is the result of the expression?'
MIN_EDGE = 1
MAX_EDGE = 100


def get_question_and_answer():
    signs = {'+': add, '-': sub, '*': mul}
    number1 = random.randint(MIN_EDGE, MAX_EDGE)
    number2 = random.randint(MIN_EDGE, MAX_EDGE)
    sign = random.choice(list(signs.keys()))
    question = '{} {} {}'.format(number1, sign, number2)
    answer = str(signs[sign](number1, number2))
    return question, answer
