#!/usr/bin/env python

from random import randint

GAMES_PURPOSE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_EDGE = 1
MAX_EDGE = 100
FIRST_PRIME_NUMBER = 2


def is_prime(number):
    if number < FIRST_PRIME_NUMBER:
        return False

    for divisor in range(FIRST_PRIME_NUMBER, number // 2):
        if number % divisor == 0:
            return False
    return True


def get_question_and_answer():
    question = randint(MIN_EDGE, MAX_EDGE)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
