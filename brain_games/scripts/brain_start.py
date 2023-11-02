#!/usr/bin/env python3
# Главный скрипт для вызова всех игр

import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


if __name__ == '__main__':
    main()
