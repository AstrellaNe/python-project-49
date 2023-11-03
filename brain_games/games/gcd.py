#!/usr/bin/env python3
# игра НОД
from random import randint
from math import gcd


TASK = 'Find the greatest common divisor of given numbers.'


def task():
    return TASK


def question_and_answer():
    number_one = randint(0, 100)
    number_two = randint(1, 10)  # 1 чтобы не было дел на 0
    question = f'Question: {number_one} {number_two}'
    correct_answer = str(gcd(number_one, number_two))
    return question, correct_answer