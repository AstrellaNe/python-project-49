#!/usr/bin/env python3
# модуль изолированного запуска прогрессии
import brain_games.game_launcher as engine
import brain_games.games.progression as prog


def main():
    engine.game_execute(prog)


if __name__ == '__main__':
    main()
