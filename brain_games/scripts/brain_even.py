import prompt
from random import randint


def main():
    count = 1
    print('Welcome to the Brain Games! ')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")


    while count <= 3:
        count += 1
        number = randint(0, 60)

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print('Question: ' + str(number))
        answer = input('Your answer: ')

        if answer == 'yes' and number % 2 == 0 and count <= 3 or \
           answer == 'no' and number % 2 == 1 and count <= 3:
            print('Correct!')
            continue
        elif answer == 'yes' and number % 2 == 1 and count <= 3 or \
             answer == 'no' and number % 2 == 0 and count <= 3:
            print("'" + answer + " ' is wrong answer ;(. Correct answer was " + correct_answer + ".\nLet's try again, " + name + "!")
            continue
        elif count > 3 and answer == correct_answer:
            print('Congratulations, ' + name + '!')
        elif count > 3 and answer != correct_answer:
            print("Let's try again, " + name + "!")
