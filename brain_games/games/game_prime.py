#!/usr/bin/env python

from random import randint

games_purpose = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_prime(numbers_question):
    if numbers_question % 2 == 0 and numbers_question != 2:
        return 'no'
    else:
        return 'yes'


def game_process():
    question = randint(1, 100)
    answer = game_prime(question)
    return question, answer
