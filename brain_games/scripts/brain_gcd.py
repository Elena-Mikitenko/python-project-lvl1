#!/usr/bin/env python

from brain_games import engine
from brain_games.games import game_gcd


def main_brain_gcd():
    engine.run_engine(game_gcd)


if __name__ == '__main__':
    main_brain_gcd()
