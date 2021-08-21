#!/usr/bin/env python

from random import randint

GAMES_PURPOSE = 'Answer "yes" if number is even, otherwise answer "no".'
MIN_EDGE = 1
MAX_EDGE = 100


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():
    question = randint(MIN_EDGE, MAX_EDGE)
    answer = 'yes' if is_even(question) else 'no'
    return question, answer
