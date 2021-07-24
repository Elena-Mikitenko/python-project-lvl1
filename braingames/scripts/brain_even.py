import prompt
from random import randint


def main():
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))


    number = randint(0, 100)


    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    print('Question: ' + str(number))
    answer = input('Your answer: ')


    if answer == 'yes' and number % 2 == 0 or answer == 'no' and number % 2 == 1:
        print('Correct!')
        return True
    else:
        print("'" + answer + " ' is wrong answer ;(. Correct answer was " + correct_answer + ".\nLet's try again " + name + "!")
        return False
