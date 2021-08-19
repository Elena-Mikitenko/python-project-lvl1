#!/usr/bin/env python

import random

GAMES_PURPOSE = 'Find the greatest common divisor of given numbers.'
MIN_EDGE = 1
MAX_EDGE = 100


def get_question_and_answer_for_game():
    first_number = random.randint(MIN_EDGE, MAX_EDGE)
    second_number = random.randint(MIN_EDGE, MAX_EDGE)
    divisor = min(first_number, second_number)
    while divisor > 0:
        divisor = divisor - 1
        if first_number % divisor == 0 and second_number % divisor == 0:
            break

    question = f'{first_number} {second_number}'
    answer = divisor
    return question, str(answer)
