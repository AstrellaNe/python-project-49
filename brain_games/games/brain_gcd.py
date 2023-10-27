#!/usr/bin/env python3
# игра НОД
from random import randint 
import brain_games.scripts.brain_isolate as isolate  # для изолиров запуска

# функция 2 рандомных чисел
def random_number_calc():
    number_one = randint(0, 100)  # ноль ставлю сознательно - так интереснее
    number_two = randint(1, 10)  # от 1, чтобы не было дел. на 0
    return number_one, number_two

def comdiv():
    number_one, number_two = random_number_calc()
    division_result = number_one // number_two  # вычисляем первый делитель
    while division_result > 0:
        if number_one % number_two == 0 and number_two % division_result == 0:
            break
        division_result -= 1  # снижаем результат на 1, чтобы проверить будет ли 0

    return number_one, number_two, division_result


def main():  # вызываем только сами функции и проверяем результат
    number_one, number_two, division_result = comdiv()
    correct_answer = division_result
    question = (f'Question: {number_one} {number_two}')
    welcome_text = '''Welcome to the Brain Games COMDIV!
Find the greatest common divisor of given numbers. Use only digits'''
    
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
        print(correct_answer) # нужно только для отладки, удалить на релизе
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
