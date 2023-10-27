#!/usr/bin/env python3

def welcome_user():
    # Приветствие пользователя
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def isolated(): # функция для работы игры изолированно
        print('''Welcome to the Brain Games Even or Odd!
Answer "yes" if the number is even, otherwise answer "no". 
Use only letters, no breaks or symbols!''')
        answers_count = 0 # Счетчик правильных ответов
        for turn in range(3):
        print(question)
        user_answer = input('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct!')
            answers_count += 1
        else:
            print(f'{user_answer} is the wrong answer ;(. The correct answer was {correct_answer}')
            break
    
    return answers_count
        name = welcome_user()
    
        answers_count = 0
        if answers_count == 3:
            print(f'Congratulations, {name}! You answered all questions correctly.')
        else:
            print(f"Let's try again, {name}!")
    
        question, correct_answer = random_number()
        return question, correct_answer 