#!/usr/bin/env python3
# Игра Чет-нечет
from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def task():
    return TASK


def question_and_answer():
    number = randint(0, 100)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = f'Question: {number}'
    return question, correct_answer
