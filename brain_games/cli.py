#!/usr/bin/env python

import prompt


def welcome_user():
    print('Welcome to the Brain games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
