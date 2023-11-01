#!/usr/bin/env python3
# Главный скрипт для вызова всех игр

import prompt
import brain_games.games.brain_calc as brain_calc
import brain_games.games.brain_even as brain_even
import brain_games.games.brain_gcd as brain_gcd
import brain_games.games.brain_progression as brain_prog
import brain_games.games.brain_prime as brain_prime

# Словарь, чтобы можно было добавить в будущем много других игр
games = {
    '1': brain_even.main,
    '2': brain_calc.main,
    '3': brain_gcd.main,
    '4': brain_prog.main,
    '5': brain_prime.main,
}


def game_choice(name):
    max_attempts = 3
    available_choices = {'1': "Even or Odd",
                         '2': "Calculator",
                         '3': "Common Divisor",
                         '4': "Progression",
                         '5': "Prime Number"}

    for attempt in range(1, max_attempts + 1):
        choice = prompt.string('''Choose a game:
            Print "1" for "Even or Odd"
            Print "2" for "Calculator"
            Print "3" for "Common Divisor"
            Print "4" for "Progression"
            Print "5" for "Prime Number":''')

        if choice in available_choices:
            chosen_game = games.get(choice)
            return chosen_game

        print(f'Invalid choice, {name}!'
              f'Please enter a number of the available games.')

        if attempt == max_attempts:
            print(f'''Sorry, {name}, too many mistakes ;(.
We end the game. Let's try again next time!''')
            return None

        print('Digits only!')


def game_cycle(chosen_game):
    max_attempts = 3
    answers_count = 0  # Counter for correct answers

    welcome_text, _, _ = chosen_game()  # Get welcome text once

    print(welcome_text)

    for turn in range(max_attempts):
        _, question, correct_answer = chosen_game()
        print(question)
        user_answer = input('Your answer: ')

        if str.lower(user_answer) == str(correct_answer):
            print('Correct!')
            answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            break

    return answers_count


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    chosen_game = game_choice(name)

    if chosen_game:
        answers_count = game_cycle(chosen_game)

        if answers_count == 3:
            print(f'Congratulations, {name}!'
                  f' You answered all questions correctly.')
        else:
            print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
