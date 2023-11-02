#!/usr/bin/env python3
# модуль изолированного запуска чет-нечет
import brain_games.scripts.brain_engine as brain_engine  # обработчик цикла
from brain_games.games.brain_even import main as even


def main():
    brain_engine.game = even
    brain_engine.main()


if __name__ == '__main__':
    main()
