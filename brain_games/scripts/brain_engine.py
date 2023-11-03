#!/usr/bin/env python3
# модуль изолированного запуска игр
import prompt

WELCOME = 'Welcome to the Brain Games!'
TURNS = 3


def game_execute(game):
    print(WELCOME)
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.task())

    for _ in range(TURNS):
        question, correct_answer = game.question_and_answer()
        print(str(question))
        user_answer = prompt.string('Your answer: ')

        if str(user_answer.lower()) == str(correct_answer):
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(.'
                  f'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            return False

    print(f'Congratulations, {name}!')
    return True


def main(game):
    game_execute(game)


if __name__ == '__main__':
    main()
