#!/usr/bin/env python3
# модуль изолированного запуска чет-нечет
import brain_games.game_launcher as engine
import brain_games.games.even as even  # Import even game module


def main():
    engine.game_execute(even)


if __name__ == '__main__':
    main()
