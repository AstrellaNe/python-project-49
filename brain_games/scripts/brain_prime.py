#!/usr/bin/env python3
# модуль изолированного запуска прогрессии
import brain_games.scripts.brain_engine as brain_engine  # обработчик цикла
from brain_games.games.brain_prime import main as prime


def main():
    brain_engine.game_cycle(prime)


if __name__ == '__main__':
    main()
