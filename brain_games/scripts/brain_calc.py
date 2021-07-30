import random
from brain_games.cli import welcome_user
from operator import add, sub, mul


def game_calc():
    name = welcome_user()
    print('What is the result of the expression?')
    count = 1
    answer = ''
    expression = ''
    random_sign = {' + ': add, ' - ': sub, ' * ': mul}

    while count <= 3:
        count += 1
        sign = list(random_sign.keys())
        number1, number2 = (random.randint(1, 100), random.randint(1, 100))
        my_char = random.choice(sign)
        expression = random_sign[my_char](number1, number2)

        print('Question: ' + str(number1) + str(my_char) + str(number2))
        answer = input('Your answer: ')

        if answer == str(expression):
            print('Correct!')
            continue
        else:
            print(("'" + str(answer) + "' is wrong answer ;(. "
                   "Correct answer was '" + str(expression) + "'.\nLet's "
                   "try again, " + name + "!"))
    if count > 3 and answer == str(expression):
        print('Congratulations, ' + name + '!')
