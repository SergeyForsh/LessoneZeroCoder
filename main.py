import arithmetic

# Пример произвольных аргументов
a = 10
b = 5

# Выполнение арифметических операций
sum_result = arithmetic.add(a, b)
subtract_result = arithmetic.subtract(a, b)
multiply_result = arithmetic.multiply(a, b)
divide_result = arithmetic.divide(a, b)

# Вывод результатов
print(f"Сложение: {a} + {b} = {sum_result}")
print(f"Вычитание: {a} - {b} = {subtract_result}")
print(f"Умножение: {a} * {b} = {multiply_result}")
print(f"Деление: {a} / {b} = {divide_result}")

# Пример деления на ноль
print(arithmetic.divide(a, 0))