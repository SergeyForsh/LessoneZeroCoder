def convert_temperature():
    print("Выберите конвертацию:")
    print("1. Цельсий в Фаренгейт")
    print("2. Фаренгейт в Цельсий")

    choice = input("Введите номер операции (1/2): ")

    if choice == '1':
        celsius = float(input("Введите температуру в градусах Цельсия: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius}°C")
    else:
        print("Неверный ввод. Пожалуйста, выберите 1 или 2.")

# Запуск программы
convert_temperature()

### Как это работает:
# 1. Программа выводит меню с двумя вариантами конвертации: из Цельсия в Фаренгейт и
# из Фаренгейта в Цельсий.
# 2. Пользователь вводит номер операции, которую он хочет выполнить.
# 3. В зависимости от выбора, программа запрашивает температуру в соответствующей шкале и
# выполняет расчет:
#  - Для конвертации из Цельсия в Фаренгейт используется формула: \( F = C \times \frac{9}{5} + 32 \)
#  - Для конвертации из Фаренгейта в Цельсий используется формула: \( C = (F - 32) \times \frac{5}{9} \)
# 4. Результат выводится на экран.
# 5. Если пользователь вводит неверный номер операции, программа сообщает об ошибке.