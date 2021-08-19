#!/usr/bin/env python

from random import randint

GAMES_PURPOSE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_EDGE = 1
MAX_EDGE = 100


def is_prime(numbers_question):
    first_prime_number = 2

    if numbers_question < first_prime_number:
        return False

    for divisor in range(2, numbers_question - 1):
        if numbers_question % divisor == 0:
            return False
        divisor += 1
    return True


def get_question_and_answer_for_game():
    question = randint(MIN_EDGE, MAX_EDGE)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
