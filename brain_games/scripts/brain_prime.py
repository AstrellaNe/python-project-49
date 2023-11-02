#!/usr/bin/env python3
# модуль изолированного запуска прогрессии
import brain_games.scripts.brain_engine as brain_engine
from brain_games.games.brain_prime import question_and_answer as prime
from brain_games.games.brain_prime import TASK as prime_TASK 

def main():
    brain_engine.game_execute(prime, prime_TASK)


if __name__ == '__main__':
    main()
