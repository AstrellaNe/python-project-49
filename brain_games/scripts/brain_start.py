#!/usr/bin/env python3
# Главный скрипт для вызова всех игр

import prompt
import brain_games.games.brain_calc as brain_calc
import brain_games.games.brain_even as brain_even
import brain_games.games.brain_gcd as brain_gcd
import brain_games.games.brain_progression as brain_prog

# Словарь, чтобы можно было добавить в будущем много других игр
games = {
    '1': brain_even.main,
    '2': brain_calc.main,
    '3': brain_gcd.main,
    '4': brain_prog.main,
}

def welcome_user():
    # Приветствие пользователя
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def game_choice(name):
    # Счетчик неверного ввода выбора игры
    non_digit_choice = 0
    chosen_game = None
    
    while chosen_game is None:
        choice = prompt.string('''Choose a game: 
        Print "1" for "Even or Odd"
        Print "2" for "Calculator"
        Print "3" for "Common Divisor"
        Print "4" for "Progression": ''')
        
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




def game_cycle(chosen_game, name):
    # Один цикл игры   
    answers_count = 0 # Счетчик правильных ответов
    
    for turn in range(3):
        welcome_text, question, correct_answer = chosen_game()
        if answers_count == 0:
            print(welcome_text)
        print(question)
        user_answer = input('Your answer: ')
        if user_answer == str(correct_answer):
            answers_count += 1
        else:
            print(f'{user_answer} is the wrong answer ;(. The correct answer was {correct_answer}')
            break
    
    return answers_count




def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    game = game_choice(name)
    if game:
        answers_count = game_cycle(game, name)  # передаем параметры выбранной игры
        if answers_count == 3:
            print(f'Congratulations, {name}! You answered all questions correctly.')
        else:
            print(f"Let's try again, {name}!")


if __name__ == '__main__':
    main()
