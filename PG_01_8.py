import random

# Задайте диапазон
min_value = int(input("Введите минимальное значение диапазона: "))
max_value = int(input("Введите максимальное значение диапазона: "))

# Генерация случайного числа
random_number = random.randint(min_value, max_value)

# Вывод случайного числа на экран
print(f"Случайное число в диапазоне от {min_value} до {max_value}: {random_number}")


# Как это работает:
# 1. Импортируется модуль `random`, который содержит функции для генерации случайных чисел.
# 2. Пользователю предлагается ввести минимальное и максимальное значения диапазона.
# 3. С помощью функции `random.randint()` генерируется случайное целое число в указанном диапазоне,
# включая границы.
# 4. Случайное число выводится на экран.
#
# Запуск программы:
# Скопируйте код в файл с расширением `.py` (например, `random_number_generator.py`) и
# выполните его в среде Python.