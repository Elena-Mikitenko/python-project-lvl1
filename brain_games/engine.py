#!/usr/bin/env python

import prompt

QUANTITY_OF_ROUNDS = 3


def run_engine(game):
    print('Welcome to the Brain Games!')
    gamer_name = prompt.string('May I have your name? ')
    print('Hello, {0}! '.format(gamer_name))

    print(game.GAMES_PURPOSE)
    count = 1

    while count <= QUANTITY_OF_ROUNDS:
        count += 1
        question, correct_answer = game.get_question_and_answer_for_game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            continue
        elif answer != correct_answer:
            print((f"'{answer}' is wrong answer ;(."
                   f"Correct answer was '{correct_answer}'"
                   f".\nLet's try again, {gamer_name}!"))
            break
        else:
            print('No Break')

    if count > QUANTITY_OF_ROUNDS and answer == correct_answer:
        print(f'Congratulations, {gamer_name}!')
