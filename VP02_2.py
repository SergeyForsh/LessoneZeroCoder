# Задача 4: Количество вариантов шифра кодового замка
from itertools import permutations


def count_combinations():
    total_count = 0
    # Перебираем все уникальные позиции для двух единиц из пяти
    for positions in permutations([0, 1, 2, 3, 4], 2):
        remaining_digits = [2, 3, 4] * 3  # Остальные цифры могут повторяться
        total_count += len(set(permutations([1, 1] + remaining_digits, 5)))
    return total_count


print("Количество различных вариантов шифра:", count_combinations())

# Задача 5: Определение количества бит для хранения дополнительных сведений
num_users = 100
storage_total_bytes = 1400


def calculate_additional_bits():
    bits_per_byte = 8
    total_bits = storage_total_bytes * bits_per_byte

    # Вычисляем минимальное количество бит на символ
    charset_size = 7  # Набор символов (Н, О, Р, С, Т, У, X)
    bits_per_char = (charset_size - 1).bit_length()

    password_length = 6
    password_bits = password_length * bits_per_char

    # Определяем бит для дополнительных сведений
    bits_per_user = total_bits // num_users
    additional_bits = bits_per_user - password_bits

    return additional_bits


print("Количество бит для хранения дополнительных сведений о каждом пользователе:", calculate_additional_bits())


# Задача 6: Поиск длины самой длинной цепочки, начинающейся и заканчивающейся на 'D'
def find_longest_chain(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
    except FileNotFoundError:
        print("Ошибка: файл не найден.")
        return 0
    except IOError:
        print("Ошибка: проблемы при чтении файла.")
        return 0

    max_length = 0
    current_length = 0
    o_count = 0
    in_chain = False

    for char in data:
        if char == 'D':
            if in_chain:
                if o_count <= 2:
                    max_length = max(max_length, current_length + 1)
                current_length = 1
                o_count = 0
            else:
                in_chain = True
                current_length = 1
        elif in_chain:
            current_length += 1
            if char == 'O':
                o_count += 1
            if o_count > 2:
                # Сброс цепочки должен происходить только после завершения текущей проверки
                in_chain = False
                o_count = 0

    return max_length


# Пример использования
filename = 'input.txt'  # Замените на ваш файл
print("Длина самой длинной цепочки:", find_longest_chain(filename))

