#!/usr/bin/env python3
# модуль изолированного запуска чет-нечет
import brain_games.brain_isolate as brain_isolate  #обработчик цикла игры
from brain_games.games.brain_even import main as even


def main():
    brain_isolate.welcome_user()
    brain_isolate.game_cycle(even)


if __name__ == '__main__':
    main()
        