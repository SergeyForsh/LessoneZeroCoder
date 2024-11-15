def arithmetic(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Ошибка: деление на ноль"
    else:
        return "Неизвестная операция"

# Примеры использования
print(arithmetic(10, 5, '+'))  # 15
print(arithmetic(10, 5, '-'))  # 5
print(arithmetic(10, 5, '*'))  # 50
print(arithmetic(10, 5, '/'))  # 2.0
print(arithmetic(10, 0, '/'))   # Ошибка: деление на ноль
print(arithmetic(10, 5, '%'))   # Неизвестная операция

# Эта функция принимает два числа и оператор, выполняет соответствующую арифметическую операцию и возвращает результат.
# Если операция не распознана или происходит деление на ноль, функция возвращает соответствующее сообщение.