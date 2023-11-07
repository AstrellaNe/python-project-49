# Игра Чет-нечет
from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def check_even_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False


def generate_game():
    number = randint(0, 100)
    answer = check_even_odd(number)
    if answer:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = f'Question: {number}'
    return question, correct_answer
