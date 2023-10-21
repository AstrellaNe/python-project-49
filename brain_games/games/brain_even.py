#!/usr/bin/env python3
# Игра Чет-нечет
import prompt
from random import randint

# Комменты для наставника и для себя
# пока оставим отдельной функцией,не внутри main() вопреки YAGNI
# эта функция не кажется избыточной, хотя можно встроить и в main()
# лучше обеспечить читаемость кода, а не запихивать все в одну функцию
def welcome_user():  
    name = prompt.string('May I have your name? ')
    return name


# выносим функцию рандомного числа из main() для читаемости
def random_number():
    number = randint(0, 100)
    if number % 2 == 0:
           answer = 'yes'
    else:
            answer = 'no'
    return number, answer


# вынесем игру в цикл по принципу одна функция - один функционал
def game_cycle():
    answers_count = 0
    for turn in range(3): # был цикл, но поменял на for...in
        number, correct_answer = random_number()
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            break
    return answers_count


def main(): # вызываем только сами функции и проверяем результат
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(f'Hello, {name}!\nAnswer "yes" if the number is even, otherwise answer "no".')
    game_result = game_cycle()
    if game_result == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"Let's try again, {name}!") 



if __name__ == '__main__':
    main()
