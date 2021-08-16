#!/usr/bin/env python

from random import randint
import math

games_purpose = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_prime(numbers_question):
    number = numbers_question
    first_prime_number = 2
    if numbers_question < first_prime_number:
        return 'no'

    while number >= first_prime_number:
        number -= 1
        divisor = math.gcd(numbers_question, number)
        if 1 < divisor < numbers_question:
            return 'no'
    return 'yes'


def game_process():
    question = randint(1, 100)
    answer = game_prime(question)
    return question, answer
