#!/usr/bin/env python3


def greet(player):
    print(f'Hello, {player}!\nWelcome to the Brain Games!')


def main():
    player = input("Introduce yourself, player! What is our name? ")  #игрок вводит имя, которое использует greet()
    greet(player)


if __name__ == '__main__':
    main()
