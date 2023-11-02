#!/usr/bin/env python3
# Игра Чет-нечет
from random import randint


TASK = 'Answer "yes" if number even, otherwise answer "no".'


# выносим функцию рандомного числа из main() для читаемости
def random_number():
    number = randint(0, 100)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    question = f'Question: {number}'
    return question, answer


def main():  # вызываем только сами функции
    return TASK, random_number()
