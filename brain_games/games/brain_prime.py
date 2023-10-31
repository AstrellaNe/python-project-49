#!/usr/bin/env python3
# игра прогрессия
from random import randint  # модуль для выбора случайного


# функция определения простоты числа
def random_number_calc():
    number = randint(0, 100)  # генерируем случайное число, 0 для интереса 
    if number < 2:  # проверка на 1 - по определению не простое
        return number, False
    
    for i in range(2, number):
        if number % i == 0:  # если нет остатка, кроме 2, то это не простое 
            return number, False
        
    return number, True


def main():  
    welcome_text = '''Welcome to the Brain Games Progression!
Answer "yes" if given number is prime. Otherwise answer "no"'''
    number, correct_answer = random_number_calc()
    
    question = number  
    correct_answer = 'yes' if correct_answer else 'no'

    
    return welcome_text, question, correct_answer