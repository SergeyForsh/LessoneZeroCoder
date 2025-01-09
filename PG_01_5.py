# Запрашиваем у пользователя ввод целого числа
number = int(input("Введите целое число: "))

# Проверяем, является ли число четным или нечетным
if number % 2 == 0:
    print(f"{number} является четным числом.")
else:
    print(f"{number} является нечетным числом.")



### Как это работает:
# 1. Программа запрашивает у пользователя ввод целого числа.
# 2. Введенное число преобразуется в тип `int`.
# 3. Затем программа использует оператор `%` (остаток от деления), чтобы проверить,
# делится ли число на 2 без остатка.
# 4. Если остаток равен 0, выводится сообщение о том, что число четное.
# В противном случае — что число нечетное.
