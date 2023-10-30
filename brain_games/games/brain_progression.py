#!/usr/bin/env python3
# игра прогрессия
from random import randint, choice  # модуль для выбора операции =,-или*


# функция прогрессии и подмены элемента на **
def random_number_calc():
    number = randint(0, 10)  # генерируем случайное начальное число для прогрессии
    step = randint(1, 5)  # случайный шаг для прогрессии
    n = randint(5, 15)  # случайное количество элементов в прогрессии
    progression = []  # создаем пустой список для хранения элементов прогрессии
    # генерируем элементы прогрессии и добавляем их в список
    for i in range(1, n+1):
        result = number + (i-1)*step
        progression.append(result)
    #print(progression)  # выводим элементы прогрессии для отладки
    
    # выбираем случайный элемент из прогрессии и заменяем его на **
    correct_answer = choice(progression)
    progression[progression.index(correct_answer)] = "**"
    
    return progression, correct_answer


def main():  
    welcome_text = '''Welcome to the Brain Games Progression!
What number is missing in the progression? Use only digits'''
    progression, correct_answer = random_number_calc()
    
    question = ' '.join(str(num) for num in progression)
    
    return welcome_text, question, correct_answer