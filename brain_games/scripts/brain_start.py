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
    # Счетчик неверного ввода выбора игры
    non_digit_choice = 0
    chosen_game = None
    
    while chosen_game is None:
        choice = prompt.string('''Choose a game: 
        Print "1" for "Even or Odd"
        Print "2" for "Calculator"
        Print "3" for "Common Divisor"
        Print "4" for "Progression"
        Print "5" for "Prime Number":''')

        if choice.isdigit():
            if choice in games:
                chosen_game = games.get(choice)
            else:
                print(f'Invalid choice! Please enter a number corresponding to the available games.')
                non_digit_choice += 1
                if non_digit_choice == 3:
                    print(f'''Sorry, {name}, too many mistakes ;(.
We end the game. Let's try again next time!''')
                    return
        else:
            print('Digits only!')
            non_digit_choice += 1
            if non_digit_choice == 3:
                print(f'''Sorry, {name}, too many mistakes ;(.
We end the game. Let's try again next time!''')
                return
    
    return chosen_game


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
