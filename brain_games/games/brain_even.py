#!/usr/bin/env python3
# Игра Чет-нечет
from random import randint
import brain_games.scripts.brain_isolate as isolate  # для изолиров запуска


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
    name = isolate.welcome_user()
    main()
    answers_count = 0
    for turn in range(3):
        welcome_text, question, correct_answer = main()
        if answers_count == 0:
            print(welcome_text)
        print(question)
        user_answer = input('Your answer: ')
        if user_answer == str(correct_answer):
            answers_count += 1
        else:
            print(f'{user_answer} is the wrong answer ;(. The correct answer was {correct_answer}')
            break
    
    if answers_count == 3:
        print(f'Congratulations, {name}! You answered all questions correctly.')
    else:
        print('Sorry, you lost. Try again!')
