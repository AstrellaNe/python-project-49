#!/usr/bin/env python3
# модуль изолированного запуска игр
import prompt

WELCOME = 'Welcome to the Brain Games!'


def game_cycle(game):
    answers_count = 0
    while answers_count < 3:
        TASK, (question, correct_answer) = game()
        print(question)
        user_answer = input('Your answer: ')
        if str.lower(user_answer) == str(correct_answer):
            print('Correct!')
            answers_count += 1
        else:
            print(f"'{user_answer}' is the wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            break
    if answers_count == 3:
        print(f'Congratulations, {NAME}!')
    else:
        print(f"Let's try again, {NAME}!")


def execute_game(game_func=None):
    global NAME
    if game_func:
        TASK, _ = game_func()  # TASK из игры
        print(TASK)
        game_cycle(game_func)
    else:
        print('No game selected.')


def main():
    global NAME, game
    print(WELCOME)
    NAME = prompt.string('May I have your name? ')
    print(f'Hello, {NAME}!')

    # Зупаскаем игру
    execute_game(game)


if __name__ == '__main__':
    main()
