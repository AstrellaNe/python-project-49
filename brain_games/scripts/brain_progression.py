#!/usr/bin/env python3
# модуль изолированного запуска прогрессии
import brain_games.scripts.brain_engine as brain_engine  # обработчик цикла
from brain_games.games.brain_progression import main as prog


def main():
    brain_engine.game = prog
    brain_engine.main()


if __name__ == '__main__':
    main()
