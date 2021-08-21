#!/usr/bin/env python

from random import randint

GAMES_PURPOSE = 'What number is missing in the progression?'

NUMBERS_IN_LINE = 10
MIN_EDGE = 1
MAX_EDGE = 100
MIN_STEP_EDGE = 5
MAX_STEP_EDGE = 30


def get_question_and_answer():
    first_number = randint(MIN_EDGE, NUMBERS_IN_LINE)
    progression_step = randint(MIN_STEP_EDGE, MAX_STEP_EDGE)
    indefinite_number = randint(1, NUMBERS_IN_LINE - 1)
    progression = [first_number + i * progression_step
                   for i in range(NUMBERS_IN_LINE)]
    answer = str(first_number + progression_step * indefinite_number)
    progression[indefinite_number] = '..'
    question = ' '.join(map(str, progression))
    return question, answer
