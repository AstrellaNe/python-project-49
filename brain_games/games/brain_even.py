#!/usr/bin/env python3
# Игра Чет-нечет
from random import randint


TASK = 'Answer "yes" if number even, otherwise answer "no".'


def question_and_answer():
    number = randint(0, 100)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'

    question = number
    return question, answer
