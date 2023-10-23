#!/usr/bin/env python3
# игра Калькулятор
import prompt
from random import randint, choice # модуль для выбора операции =,-или*

# Комменты для наставника и для себя
# пока оставим отдельной функцией,не внутри main() вопреки YAGNI
# эта функция не кажется избыточной, хотя можно встроить и в main()
# лучше обеспечить читаемость кода, а не запихивать все в одну функцию
def welcome_user():  
    name = prompt.string('May I have your name? ')
    return name


# функция 2 рандомных чисел  верный ответ в зависимости от операции 
def random_number_calc(operation):
    number_one = randint(0, 100) # ноль ставлю сознательно - так интереснее
    number_two = randint(0, 10) # пока малые числа иначе не игра, а мучение при отладке
    
    if operation == '+':
        calc_answer = number_one + number_two
    elif operation == '-':
        calc_answer = number_one - number_two
    else:
        calc_answer = number_one * number_two
    
    return (number_one, number_two), calc_answer


# вынесем игру в цикл по принципу одна функция - один функционал
def game_cycle_calc():
    answers_count = 0
    non_digit_count = 0 #подсчет ошибки в типе данных при ответе
    for turn in range(3):
        operation = choice(['+', '-', '*']) #модуль из random для рандомной операции
        (number_one, number_two), correct_answer = random_number_calc(operation)
        print(f'Question: {number_one} {operation} {number_two}')
        
        while True: # проверка на идиота. 2 раза-случайность, 3 -закономерность
            user_answer = input('Your answer: ')
            if user_answer.isdigit():
                user_answer = int(user_answer)
                break
            else:
                print('Only digits!')
                non_digit_count += 1
                if non_digit_count == 3:
                    break
                
        if user_answer == correct_answer:
            print('Correct!')
            answers_count += 1
        else:
            print(f"'{user_answer}' is the wrong answer ;(. The correct answer was '{correct_answer}'.")
            break
    return answers_count


def main(): # вызываем только сами функции и проверяем результат
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!\nWhat is the result of the expression?. Use only digits')
    game_result = game_cycle_calc()
    if game_result == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!") 



if __name__ == '__main__':
    main()
