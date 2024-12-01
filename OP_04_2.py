import math

def square(side_length):
    perimeter = 4 * side_length
    area = side_length ** 2
    diagonal = math.sqrt(2) * side_length
    return perimeter, area, diagonal

# Пример использования функции
side = 5
perimeter, area, diagonal = square(side)
print(f"Периметр: {perimeter}, Площадь: {area}, Диагональ: {diagonal}")



# В этом коде:
# - Периметр квадрата рассчитывается как \(4 \times \text{сторона}\).
# - Площадь квадрата рассчитывается как \(\text{сторона}^2\).
# - Диагональ квадрата рассчитывается по формуле \( \text{сторона} \times \sqrt{2} \).
#
# Вы можете вызывать эту функцию с любой длиной стороны квадрата, и она вернет соответствующие значения.