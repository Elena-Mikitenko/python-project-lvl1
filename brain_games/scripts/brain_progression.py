import random
import prompt
from brain_games.cli import welcome_user


def game_progression():
    name = welcome_user()
    print('What number is missing in the progression? ')

    for count in range(0, 3):
        step = random.randint(1, 20)
        beg = random.randint(1, 20)
        number = random.randint(0, 9)
        num_line = [count for count in range(beg, beg + ((step * 9) + 1), step)]
        which_number = num_line[number]
        num_line[number] = '..'
        my_string = ' '.join(map(str, num_line))
        print('Question: {}'.format(my_string))
        answer = prompt.integer('Your answer: ')

        if answer == which_number:
            print('Correct!')
        else:
            print(("'" + str(answer) + "' is wrong answer ;(. "
                   "Correct answer was'" + str(which_number) + ""
                   "'. \nLet's try again, " + name + "!"))

        if count >= 2 and answer == which_number:
            print('Congratulations, ' + name + '!')
