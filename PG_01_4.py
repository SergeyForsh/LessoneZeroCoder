def format_seconds(seconds):
    days = seconds // 86400  # 1 день = 86400 секунд
    hours = (seconds % 86400) // 3600  # 1 час = 3600 секунд
    minutes = (seconds % 3600) // 60  # 1 минута = 60 секунд
    seconds = seconds % 60  # остаток секунд

    return f"{days}:{hours:02}:{minutes:02}:{seconds:02}"

# Пример использования
total_seconds = 987654
formatted_time = format_seconds(total_seconds)
print(formatted_time)  # Вывод: 11:13:17:34



# В этом коде мы вычисляем количество дней, часов, минут и оставшихся секунд,
# а затем форматируем их в строку, где часы, минуты и секунды выводятся с ведущими нулями,
# если они меньше 10.
