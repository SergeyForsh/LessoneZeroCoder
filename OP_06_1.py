
user_input = input("Введите текст, который вы хотите сохранить в файл: ")

# Открываем файл user_data.txt для записи

with open('user_data.txt', 'w') as file:
    file.write(user_input)
    # Записываем введенный текст в файл

print("Ваш текст успешно сохранен в файле user_data.txt.")


