#!/usr/bin/env python3
# модуль изолированного запуска калькулятора
import brain_games.game_launcher as engine
import brain_games.games.gcd as gcd


def main():
    engine.game_execute(gcd)


if __name__ == '__main__':
    main()
