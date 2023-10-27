#!/usr/bin/env python3
# игра Калькулятор
from random import randint, choice  # модуль для выбора операции =,-или*
import brain_games.scripts.brain_isolate as isolate  # для изолиров запуска

# функция 2 рандомных чисел и верный ответ в зависимости от операции
def random_number_calc(operation):
    number_one = randint(0, 10)  # ноль ставлю сознательно - так интереснее
    number_two = randint(0, 10)  # пока малые числа для легкой отладки
    if operation == '+':
        calc_answer = number_one + number_two
    elif operation == '-':
        calc_answer = number_one - number_two
    else:
        calc_answer = number_one * number_two
    question = f'Question: {number_one} {operation} {number_two}'
    return question, calc_answer


def main():  # вызываем только сами функции и проверяем результат
    welcome_text = '''Welcome to the Brain Games Calculator!
What is the result of the expression? Use only digits'''
    operation = choice(['+', '-', '*'])
    question, correct_answer = random_number_calc(operation)

    return welcome_text, question, correct_answer


if __name__ == '__main__':
    name = isolate.welcome_user()
    main()
    answers_count = 0
    for turn in range(3):
        welcome_text, question, correct_answer = main()
        if answers_count == 0:
            print(welcome_text)
        print(question)
        user_answer = input('Your answer: ')
        if user_answer == str(correct_answer):
            answers_count += 1
        else:
            print(f'{user_answer} is the wrong answer ;(. The correct answer was {correct_answer}')
            break
    
    if answers_count == 3:
        print(f'Congratulations, {name}! You answered all questions correctly.')
    else:
        print('Sorry, you lost. Try again!')
