#!/usr/bin/env python

from random import randint

games_purpose = 'Answer "yes" if number is even, otherwise answer "no".'


def game_even(numbers_question):
    if numbers_question % 2 == 0:
        return 'yes'
    else:
        return 'no'


def game_process():
    question = randint(1, 100)
    answer = game_even(question)
    return question, answer
