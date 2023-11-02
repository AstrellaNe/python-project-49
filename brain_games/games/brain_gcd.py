#!/usr/bin/env python3
# игра НОД
from random import randint
from math import gcd


# функция 2 рандомных чисел
def random_number_calc():
    number_one = randint(0, 100)  # ноль ставлю сознательно - так интереснее
    number_two = randint(1, 10)  # от 1, чтобы не было дел. на 0
    divisor = gcd(number_one, number_two)
    return number_one, number_two, divisor


# def comdiv():   нашел в модуле math готовое решение,
# это оставлю как память о собственных вычислениях до проверки
# number_one, number_two = random_number_calc()
# division_result = min(number_one, number_two)  # вычисляем первый делитель
# while division_result != 0:
#    if number_one % division_result == 0 and number_two % division_result == 0:
#         break
#     division_result -= 1  # снижаем результат на 1, чтобы проверить будет ли 0

# return number_one, number_two, division_result


def main():  # вызываем только сами функции и проверяем результат
    number_one, number_two, divisor = random_number_calc()
    correct_answer = divisor
    question = (f'Question: {number_one} {number_two}')
    welcome_text = ('Find the greatest common divisor of '
                    'given numbers.')
    return welcome_text, question, correct_answer
