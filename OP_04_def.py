def sum_range(start, end):
    # Проверяем, что start меньше или равен end
    if start > end:
        return 0  # Можно вернуть 0 или обработать ошибку, если start больше end

    total = 0
    for number in range(start, end + 1):
        total += number

    return total


# Пример использования
result = sum_range(10, 15)
print(f"Сумма чисел от 10 до 15: {result}")  # Вывод: 15

### Объяснение:
# 1. Функция принимает два аргумента: `start` и `end`.
# 2. Если `start` больше `end`, функция возвращает `0` (это можно изменить в зависимости от требований).
# 3. В цикле `for` происходит суммирование всех целых чисел в диапазоне от `start` до `end` включительно.
# 4. Результат возвращается и выводится на экран.

# Вы можете протестировать функцию с различными значениями `start` и `end`!

print()

def sum_range(start, end):
    summ = 0
    if start > end:
        print("Неверные аргументы!")
        return summ

    for i in range(start,end+1):
        summ += i
    return summ


start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))
print("Сумма чисел от " + str(start) + " до " + str(end) + " равна: " + str(sum_range(start, end)))
