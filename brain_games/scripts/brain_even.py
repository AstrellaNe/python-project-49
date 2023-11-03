#!/usr/bin/env python3
# модуль изолированного запуска чет-нечет
import brain_games.scripts.brain_engine as engine
import brain_games.games.even as even  # Import even game module


def main():
    engine.main(even)


if __name__ == '__main__':
    main()
