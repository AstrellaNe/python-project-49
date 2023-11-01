#!/usr/bin/env python3
# модуль изолированного запуска прогрессии
import brain_games.scripts.brain_isolate as brain_isolate  # обработчик цикла
from brain_games.games.brain_progression import main as prog


def main():
    brain_isolate.game_cycle(prog)


if __name__ == '__main__':
    main()
