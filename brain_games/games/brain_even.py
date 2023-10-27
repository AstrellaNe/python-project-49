#!/usr/bin/env python3
# Игра Чет-нечет
from random import randint


# выносим функцию рандомного числа из main() для читаемости
def random_number():
    number = randint(0, 100)
    if number % 2 == 0:
           answer = 'yes'
    else:
            answer = 'no'

    question = f'Question: {number}'
    return question, answer


def main():  # вызываем только сами функции 
    welcome_text = ''''Welcome to the Brain Games Even or Odd!
Answer "yes" if the number is even, otherwise answer "no".
Use only letters, no breaks or symbols!'''
    question, correct_answer = random_number()

    return welcome_text, question, correct_answer 


if __name__ == '__main__':
    main()
