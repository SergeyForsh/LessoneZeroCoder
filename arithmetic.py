def add(a, b):
    """Сложение двух чисел."""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел."""
    return a - b

def multiply(a, b):
    """Умножение двух чисел."""
    return a * b

def divide(a, b):
    """Деление двух чисел."""
    if b == 0:
        return "Ошибка: Деление на ноль!"
    return a / b