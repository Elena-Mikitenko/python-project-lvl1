#!/usr/bin/env python

from random import randint
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    count = 1
    answer = ''
    correct_answer = ''
    while count <= 3:
        count += 1
        number = randint(0, 60)

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('Question: ' + str(number))
        answer = input('Your answer: ')

        if answer == 'yes' and number % 2 == 0 or\
                answer == 'no' and number % 2 == 1:
            print('Correct!')
            continue
        else:
            print(("'" + answer + " ' is wrong answer ;(."
                   "Correct answer was " + correct_answer + ".\nLet's "
                   "try again, " + name + "!"))
            continue
    if count > 3 and answer == correct_answer:
        print('Congratulations, ' + name + '!')
