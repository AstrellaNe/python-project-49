#!/usr/bin/env python3
# игра Калькулятор
from random import randint, choice  # модуль для выбора операции =,-или*


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