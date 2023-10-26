#!/usr/bin/env python3
# игра НОД
from random import randint 


# функция 2 рандомных чисел 
def random_number_calc():
    number_one = randint(0, 100) # ноль ставлю сознательно - так интереснее
    number_two = randint(1, 10) # от 1, чтобы не было дел. на 0
    return number_one, number_two

def comdiv():
    number_one, number_two = random_number_calc()
    division_result = number_one // number_two #вычисляем первый делитель
    while division_result > 0:
        if number_one % number_two == 0 and number_two % division_result == 0:
            break
        division_result -= 1 # снижаем результат на 1, чтобы проверить будет ли 0       
    
    return number_one, number_two, division_result


def main(): # вызываем только сами функции и проверяем результат
    number_one, number_two, division_result = comdiv()
    correct_answer = division_result
    question = (f'Question: {number_one} {number_two}')
    print('Welcome to the Brain Games COMDIV!\nFind the greatest common divisor of given numbers. Use only digits')
    print(question)
    return correct_answer


if __name__ == '__main__':
    main()
