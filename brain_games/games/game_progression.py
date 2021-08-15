#!/usr/bin/env python

import random
from itertools import count, islice

games_purpose = 'What number is missing in the progression?'

NUMBERS_IN_LINE = 10


def game_process():
    progression = list(islice(count(
        start=random.randint(1, 100),
        step=random.randint(1, 10)), NUMBERS_IN_LINE))
    answer = random.choice(progression)
    indefinite_number = progression.index(answer)
    progression[indefinite_number] = '..'
    for i, _ in enumerate(progression):
        progression[i] = str(progression[i])
    question = ' '.join(progression)
    return question, str(answer)
