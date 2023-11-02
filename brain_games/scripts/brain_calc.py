#!/usr/bin/env python3
# модуль изолированного запуска калькулятора
import brain_games.scripts.brain_engine as brain_engine  # обработчик цикла
from brain_games.games.brain_calc import main as calc


def main():
    brain_engine.game = calc
    brain_engine.main()


if __name__ == '__main__':
    main()
