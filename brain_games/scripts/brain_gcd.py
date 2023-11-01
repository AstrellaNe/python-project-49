#!/usr/bin/env python3
# модуль изолированного запуска калькулятора
import brain_games.scripts.brain_isolate as brain_isolate  # обработчик цикла
from brain_games.games.brain_gcd import main as gcd


def main():
    name = brain_isolate.welcome_user()
    brain_isolate.game_cycle(gcd, name)


if __name__ == '__main__':
    main()
