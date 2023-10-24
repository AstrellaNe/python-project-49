#!/usr/bin/env python3
# игра Калькулятор
import prompt
from random import randint, choice # модуль для выбора операции =,-или*


# функция 2 рандомных чисел и верный ответ в зависимости от операции 
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


#проверка на ввод только цифр и передача переменной user_answer из game_cycle
def goofy_check(user_answer): 
    if user_answer.isdigit():
        return int(user_answer)
    else:
        return 'non_digit'

def game_cycle_calc():
    answers_count = 0
    for turn in range(3):
        operation = choice(['+', '-', '*'])
        (number_one, number_two), correct_answer = random_number_calc(operation)
        print(f'Question: {number_one} {operation} {number_two}')
        user_answer = input('Your answer: ') #переназначаем перемен для ввода игроком
        result = goofy_check(user_answer) #делаем проверку переменной на int       
        non_digit_count = 0
        if result == 'non_digit':
            non_digit_count += 1
            print('Only digits!')
            if non_digit_count == 3: 
                print('You entered non-digits instead of digits 3 times. Sorry, the game is over.')
                return answers_count #передаем нулевой счетчик
        elif result != correct_answer:
            print(f"'{result}' is the wrong answer ;(. The correct answer was '{correct_answer}'.")
            return
        else:
            print('Correct!')
            answers_count += 1

  
    return str(answers_count)




def main(): # вызываем только сами функции и проверяем результат
    print('Welcome to the Brain Games Calculator!\nWhat is the result of the expression? Use only digits')
    game_result = game_cycle_calc()
    return game_result




if __name__ == '__main__':
    main()
