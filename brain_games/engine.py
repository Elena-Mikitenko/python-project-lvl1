#!/usr/bin/env python

import prompt


def greeting():
    print('Welcome to the Brain Games!')
    gamer_name = prompt.string('May I have your name? ')
    print('Hello, {0}! '.format(gamer_name))
    return gamer_name


def run_engine(some_game):
    gamer_name = greeting()
    print(some_game.games_purpose)
    quantity_of_counts = 3
    count = 1

    while count <= quantity_of_counts:
        question, correct_answer = some_game.game_process()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer != correct_answer:
            print((f"'{answer}' is wrong answer ;(."
                   f"Correct answer was '{correct_answer}'"
                   f".\nLet's try again, {gamer_name}!"))
            break
        print('Correct!')
        count += 1
    else:
        print(f'Congratulations, {gamer_name}!')
