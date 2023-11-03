#!/usr/bin/env python3
# игра прогрессия
from random import randint, choice  # модуль для выбора операции =,-или*


TASK = 'What number is missing in the progression?'


def task():
    return TASK


# функция прогрессии и подмены элемента на **
def question_and_answer():
    number = randint(0, 10)  # генерируем случайное начальное число
    step = randint(1, 5)  # случайный шаг для прогрессии
    n = randint(5, 15)  # случайное количество элементов в прогрессии
    progression = []  # создаем пустой список для хранения элементов прогрессии
    # генерируем элементы прогрессии и добавляем их в список
    for i in range(1, n + 1):
        result = number + (i - 1) * step
        progression.append(result)
    # print(progression)  # выводим элементы прогрессии для отладки

    # выбираем случайный элемент из прогрессии и заменяем его на **
    correct_answer = choice(progression)
    progression[progression.index(correct_answer)] = ".."
    question = 'Question: ' + ' '.join(str(num) for num in progression)
    return question, correct_answer
