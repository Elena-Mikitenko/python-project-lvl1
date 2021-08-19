#!/usr/bin/env python

import random
from operator import add, sub, mul

GAMES_PURPOSE = 'What is the result of the expression?'
MIN_EDGE = 1
MAX_EDGE = 100

def get_question_and_answer_for_game():
    signs = {'+': add, '-': sub, '*': mul}
    number1, number2 = random.randint(MIN_EDGE, MAX_EDGE), random.randint(MIN_EDGE, MAX_EDGE)
    signs_set = list(signs.keys())
    my_char = random.choice(signs_set)
    question = '{} {} {}'.format(number1, my_char, number2)
    answer = str(signs[my_char](number1, number2))
    return question, answer
