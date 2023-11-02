#!/usr/bin/env python3
# модуль изолированного запуска прогрессии
import brain_games.scripts.brain_engine as brain_engine
from brain_games.games.brain_progression import question_and_answer as prog
from brain_games.games.brain_progression import TASK as prog_TASK 

def main():
    brain_engine.game_execute(prog, prog_TASK)


if __name__ == '__main__':
    main()
