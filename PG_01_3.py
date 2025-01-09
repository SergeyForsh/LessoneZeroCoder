from fractions import Fraction

# Заданное вещественное число
number = 14.375

# Преобразуем вещественное число в обыкновенную дробь
fraction = Fraction(number).limit_denominator()

# Выводим результат в нужном формате
print(f"{number} = {fraction.numerator}/{fraction.denominator}")


### Как работает этот код:
# 1. Импортируем класс `Fraction` из модуля `fractions`, который позволяет работать с обыкновенными дробями.
# 2. Задаем вещественное число `number`, равное 14.375.
# 3. Преобразуем число в дробь с помощью `Fraction(number)` и используем метод `limit_denominator()`
# для получения наименьшей дроби.
# 4. Выводим результат, используя форматированный вывод.
