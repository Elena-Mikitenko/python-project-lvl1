#!/usr/bin/env python

from random import randint

games_purpose = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_prime(numbers_question):
    first_prime_number = 2
    if numbers_question < first_prime_number:
        return 'no'
    divisor = 2
    while divisor < numbers_question:
        if numbers_question % divisor == 0:
            return 'no'
        divisor += 1
    return 'yes'


def game_process():
    question = randint(1, 100)
    answer = game_prime(question)
    return question, answer
