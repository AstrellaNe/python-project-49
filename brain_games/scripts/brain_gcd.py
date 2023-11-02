#!/usr/bin/env python3
# модуль изолированного запуска калькулятора
import brain_games.scripts.brain_engine as brain_engine
from brain_games.games.brain_gcd import question_and_answer as gcd
from brain_games.games.brain_gcd import TASK as gcd_TASK 

def main():
    brain_engine.game_execute(gcd, gcd_TASK)


if __name__ == '__main__':
    main()
