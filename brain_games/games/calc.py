# игра Калькулятор
from random import randint, choice  # модуль для выбора операции =,-или*


TASK = 'What is the result of the expression?'


# Вычисление правильного ответа
def calculate_answer(number_one, number_two, operation):
    if operation == '+':
        return number_one + number_two
    elif operation == '-':
        return number_one - number_two
    else:
        return number_one * number_two


def generate_game():
    number_one = randint(0, 10)
    number_two = randint(0, 10)
    operation = choice(['+', '-', '*'])
    correct_answer = calculate_answer(number_one, number_two, operation)
    question = f'Question: {number_one} {operation} {number_two}'
    return str(question), correct_answer
