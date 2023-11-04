# игра НОД
from random import randint
from math import gcd


TASK = 'Find the greatest common divisor of given numbers.'


def generate_game():
    number_one = randint(0, 100)
    number_two = randint(1, 10)  # 1 чтобы не было дел на 0
    question = f'Question: {number_one} {number_two}'
    correct_answer = str(gcd(number_one, number_two))
    return str(question), correct_answer
