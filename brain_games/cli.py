#!/usr/bin/env python

import prompt

def welcome_user():
    print("Welcome to the Brain Games, my friend!")
    name = prompt.string('May I have your name? ')
    print('Hello, {}'.format(name))
    return name

def main(): welcome_user()

if __name__ == 'main':
    main()