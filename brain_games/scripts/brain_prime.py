#!/usr/bin/env python3
# модуль изолированного запуска прогрессии
import brain_games.scripts.brain_engine as engine
import brain_games.games.prime as prime


def main():
    engine.game_execute(prime)


if __name__ == '__main__':
    main()
