# игра прогрессия
from random import randint, choice  # модуль для выбора операции =,-или*


TASK = 'What number is missing in the progression?'


# Функция для генерации последовательности
def generate_progression():
    number = randint(0, 10)  # генерируем случайное начальное число
    step = randint(1, 5)  # случайный шаг для прогрессии
    n = randint(5, 15)  # случайное количество элементов в прогрессии
    progression = []  # создаем пустой список для хранения элементов прогрессии
    # генерируем элементы прогрессии и добавляем их в список
    for i in range(1, n + 1):
        result = number + (i - 1) * step
        progression.append(result)
    return progression


# Объединеняем последовательности и правильный ответ
def generate_game():
    progression = generate_progression()
    # выбираем случайный элемент из прогрессии и заменяем его на ".."
    modified_progression = progression[:]
    correct_answer = choice(modified_progression)
    modified_progression[modified_progression.index(correct_answer)] = ".."
    question = 'Question: ' + ' '.join(str(num) for num in modified_progression)
    return str(question), correct_answer
