#!/usr/bin/env python3
# модуль изолированного запуска чет-нечет
import brain_games.scripts.brain_isolate as brain_isolate  # обработчик цикла
from brain_games.games.brain_even import main as even


def main():
    brain_isolate.game_cycle(even)


if __name__ == '__main__':
    main()
