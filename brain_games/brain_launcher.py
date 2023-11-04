#!/usr/bin/env python3
# модуль изолированного запуска игр
import prompt

TURNS = 3


def game_execute(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.TASK)

    for _ in range(TURNS):
        question, correct_answer = game.generate_game()
        print(question)
        user_answer = prompt.string('Your answer: ')

        if user_answer.lower() == str(correct_answer):
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(.'
                  f'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
    return
