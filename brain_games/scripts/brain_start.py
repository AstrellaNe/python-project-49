#!/usr/bin/env python3
# Главный скрипт для вызова всех игр

import prompt
import brain_games.games.brain_calc as brain_calc
import brain_games.games.brain_even as brain_even
import brain_games.games.brain_gcd as brain_gcd
import brain_games.games.brain_progression as brain_prog
import brain_games.games.brain_prime as brain_prime
import brain_games.scripts.brain_isolate as isolate

# Словарь, чтобы можно было добавить в будущем много других игр
games = {
    '1': brain_even.main,
    '2': brain_calc.main,
    '3': brain_gcd.main,
    '4': brain_prog.main,
    '5': brain_prime.main,
}


def game_choice(name):
    # Счетчик неверного ввода выбора игры
    non_digit_choice = 0

    chosen_game = prompt.string('''Choose a game:
        Print "1" for "Even or Odd"
        Print "2" for "Calculator"
        Print "3" for "Common Divisor"
        Print "4" for "Progression"
        Print "5" for "Prime Number": ''')

    if chosen_game.isdigit() and chosen_game in games:
        return chosen_game
    else:
        while non_digit_choice < 2:
            print(f'Invalid choice, {name}!'
                  f'Please enter a number of the available games.')
            non_digit_choice += 1
            chosen_game = prompt.string('Choose a game:')
            if chosen_game.isdigit() and chosen_game in games:
                return chosen_game

    print(f'''Sorry, {name}, too many mistakes ;(.
  We end the game. Let's try again next time!''')
    return None


def game_cycle(chosen_game, name):
    # Один цикл игры
    answers_count = 0  # Счетчик правильных ответов

    for turn in range(3):
        game_function = games[chosen_game]
        welcome_text, question, correct_answer = game_function()
        if answers_count == 0:
            print(welcome_text)
        print(question)
        user_answer = input('Your answer: ')
        if str.lower(user_answer) == str(correct_answer):
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
    game_function = games[chosen_game]  # Получаю функцию
    isolate.game_cycle(game_function, name)  # Передаю функцию


if __name__ == '__main__':
    main()
