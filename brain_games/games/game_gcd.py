#!/usr/bin/env python

import random

GAMES_PURPOSE = 'Find the greatest common divisor of given numbers.'
MIN_EDGE = 1
MAX_EDGE = 100


def calculate_gcd(first_number, second_number):
    divisor = min(first_number, second_number)
    while divisor > 0:
        if first_number % divisor == 0 and second_number % divisor == 0:
            break
        divisor = divisor - 1
    return divisor


def get_question_and_answer():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = f'{first_number} {second_number}'
    answer = calculate_gcd(first_number, second_number)
    return question, str(answer)
