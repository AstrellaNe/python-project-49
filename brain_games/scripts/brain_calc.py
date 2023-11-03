#!/usr/bin/env python3
# модуль изолированного запуска калькулятора
import brain_games.scripts.brain_engine as engine
import brain_games.games.calc as calc


def main():
    engine.game_execute(calc)


if __name__ == '__main__':
    main()
