#!/usr/bin/env python3
# игра прогрессия
from random import randint  # модуль для выбора случайного

TASK = (
    'Answer "yes" if given number is prime.'
    ' Otherwise answer "no".'
)


def task():
    return TASK


# функция определения простоты числа
def is_prime(number):
    if number < 2:  # проверка на 1 - по определению не простое
        return False

    for i in range(2, number):
        if number % i == 0:  # если нет остатка, кроме 2, то это не простое
            return False

    return True


def question_and_answer():
    number = randint(0, 100)  # генерируем случайное число, 0 для интереса
    question = f'Question: {number}'
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
