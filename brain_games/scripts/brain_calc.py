#!/usr/bin/env python3
# модуль изолированного запуска калькулятора
import brain_games.brain_isolate as brain_isolate  #обработчик цикла игры
from brain_games.games.brain_calc import main as calc


def main():
    brain_isolate.welcome_user()
    brain_isolate.game_cycle(calc)


if __name__ == '__main__':
    main()
        