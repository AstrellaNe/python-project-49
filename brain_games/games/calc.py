# игра Калькулятор
from random import randint, choice  # модуль для выбора операции =,-или*


TASK = 'What is the result of the expression?'


# функция 2 рандомных чисел и верный ответ в зависимости от операции
def generate_game():
    number_one = randint(0, 10)  # ноль ставлю сознательно - так интереснее
    number_two = randint(0, 10)  # пока малые числа для легкой отладки
    operation = choice(['+', '-', '*'])
    if operation == '+':
        correct_answer = number_one + number_two
    elif operation == '-':
        correct_answer = number_one - number_two
    else:
        correct_answer = number_one * number_two
    question = f'Question: {number_one} {operation} {number_two}'
    return str(question), correct_answer
