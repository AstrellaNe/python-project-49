#!/usr/bin/env python3
# модуль изолированного запуска чет-нечет
import brain_games.scripts.brain_engine as brain_engine
from brain_games.games.brain_even import question_and_answer as even
from brain_games.games.brain_even import TASK as even_TASK 

def main():
    brain_engine.game_execute(even, even_TASK)


if __name__ == '__main__':
    main()
