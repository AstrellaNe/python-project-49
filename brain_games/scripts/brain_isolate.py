#!/usr/bin/env python3
import prompt
def welcome_user():
    # Приветствие пользователя
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name         
