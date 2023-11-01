#!/usr/bin/env python3
# модуль изолированного запуска калькулятора
import brain_games.scripts.brain_isolate as brain_isolate  # обработчик цикла
from brain_games.games.brain_calc import main as calc


def main():
    brain_isolate.game_cycle(calc)


if __name__ == '__main__':
    main()
