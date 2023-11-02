#!/usr/bin/env python3
# модуль изолированного запуска калькулятора
import brain_games.scripts.brain_engine as engine
import brain_games.scripts.brain_start as start
from brain_games.games.brain_calc import question_and_answer as calc
from brain_games.games.brain_calc import TASK as calc_TASK 

def main():
    start.main()
    engine.game_execute(calc, calc_TASK)


if __name__ == '__main__':
    main()
