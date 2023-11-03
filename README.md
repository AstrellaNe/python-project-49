### Hexlet tests and linter status:
[![Actions Status](https://github.com/AstrellaNe/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/AstrellaNe/python-project-49/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/5b708b6a35bdd06dc8d4/maintainability)](https://codeclimate.com/github/AstrellaNe/python-project-49/maintainability)



# Brain Games

Brain Games - это набор из 5 простых математических игр для тренировки мозга или расслабления.

## Игры


1. **Brain Even**: Ответьте, является ли число четным. Игра дает случайно число.\
Необходимо ответить yes (если четное) или no (если нечетное).\
Вводить только слова 'yes' или 'no'.

2. **Brain Calc**: Решите арифметическую задачу ("+", "-" или "*").\
Решите простой пример. Игра дает два случайных числа и операцию над ними.\
Арифметическая операция выбирается случайным образом.\
Вводить только цифры.

3. **Brain GCD**: Найдите **наибольший** общий делитель двух чисел (НОД).\
Игра дает два случайных числа. Найдите их **наибольший** общий делитель.\
Вводить только цифры.

4. **Brain Progression**: Найдите пропущенное число в арифметической прогрессии.\
Найдите скрытое с помощью __..__ число в прогрессии. Прогрессия формируется случайным образом \
Вводить только цифры.

5. **Brain Prime**: Ответьте, является ли число простым.\
Игра дает случайно число. Необходимо ответить yes (если четное) или no (если нечетное).\
Вводить только слова 'yes' или 'no'.

### Логика игры
Игра строится следующим образом:
1. Игроку дается 3 вопроса.
2. Игрок вводит ответы с клавиатуры (цифры или буквы, в зависимости от игры)
3. При 3х верных ответах игра считается пройденной и заканчивается.
4. При любом неверном ответе игра мгновенно прекращается.

## Требования
### Сборка осуществлена на Python 3.10. Ожидается, что основной фукнционал игр будет работать и на версиях от 3.6, однако работоспособность на версиях ниже 3.10 не проверялась.
- Python 3.6 и выше
- Poetry (если вы хотите использовать код для изменения, разработки или тестирования)



## Установка для простого использования
1. Клонируйте репозиторий с играми:

    git clone https://github.com/AstrellaNe/python-project-49

2. Перейдите в директорию с играми (из той директории, в которую клонировали репозиторий):

    cd brain_games

3. Установите пакет игр из директории brain_games:

 ### make package-install  (из локальной директории репозитория brain_games)

    _Примечание: эта команда использует метод pip install --user_
    
или

### make package-reinstall (для перестустановки с --force)

    _Примечание: Если вы установили пакет игр правильно (через 'pip install --user'), все команды должны работать с помощью команд напрямую из директории игр._
    _Например, для запуска игры Brain Calc внутри директории brain_games используйте команду 'brain-calc'._

#### Список команд:
- `brain-games`: Запуск заглавного скрипта для знакомства.
- `brain-even`: Запуск игры "Brain Even".
- `brain-calc`: Запуск игры "Brain Calc".
- `brain-gcd`: Запуск игры "Brain GCD".
- `brain-prog`: Запуск игры "Brain Progression".
- `brain-prime`: Запуск игры "Brain Prime".




## Установка для разработчика

1. Установите Poetry, если его у вас еще нет:

   curl -sSL https://install.python-poetry.org | python3 -

2. Клонируйте репозиторий с играми в желаемую директорию:

    git clone https://github.com/your-username/brain-games.git

3. Перейдите в директорию с играми:

    cd директория/brain-games

4. Установите зависимости: (для разработчиков и тестировщиков)

    poetry install

5. Установите пакет игр:

    make package-install
или
    make package-reinstall (для перестустановки с --force)



**Brain Games Installation and Operation check**
[![asciicast](https://asciinema.org/a/ITIguCrnkFxIdJ99E9CkGI8gH.svg)](https://asciinema.org/a/ITIguCrnkFxIdJ99E9CkGI8gH)

**Presentation of Brain Even or Odd gameplay**
[![asciicast](https://asciinema.org/a/RRiq04vt5LzNhf46gis52RokM.svg)](https://asciinema.org/a/RRiq04vt5LzNhf46gis52RokM)

**Presentation of Brain Calculator gameplay**
[![asciicast](https://asciinema.org/a/hrZ59uKwTc9dUUhLWj7KHWHhQ.svg)](https://asciinema.org/a/hrZ59uKwTc9dUUhLWj7KHWHhQ)

**Presentation of Brain GCD Module gameplay**
[![asciicast](https://asciinema.org/a/pDiJAPqz7GD8lodbcdiWKDFCM.svg)](https://asciinema.org/a/pDiJAPqz7GD8lodbcdiWKDFCM)

**Presentation of Brain Progression Module gameplay**
[![asciicast](https://asciinema.org/a/COxgFbgiwHMKyYGaWuq16f0JA.svg)](https://asciinema.org/a/COxgFbgiwHMKyYGaWuq16f0JA)

**Presentation of Brain Prime Number Module gameplay**
[![asciicast](https://asciinema.org/a/gybjMHYq1m9zEsXveAfKBCMHV.svg)](https://asciinema.org/a/gybjMHYq1m9zEsXveAfKBCMHV)

**Presentation of Brain Main Module operation**
[![asciicast](https://asciinema.org/a/vEWonqndJBFODsPgEQn7WF1Ct.svg)](https://asciinema.org/a/vEWonqndJBFODsPgEQn7WF1Ct)