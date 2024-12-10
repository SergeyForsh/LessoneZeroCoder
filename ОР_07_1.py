import tkinter as tk

def greet():
    name = name_entry.get()  # Получаем имя из текстового поля
    greeting_label.config(text=f"Привет, {name}!")  # Обновляем текст метки
# Создаем главное окно
root = tk.Tk()
root.title("Приветствие")
# Создаем метку с инструкцией
instruction_label = tk.Label(root, text="Введите ваше имя:")
instruction_label.pack(pady=10)
# Создаем текстовое поле для ввода имени
name_entry = tk.Entry(root)
name_entry.pack(pady=5)
# Создаем кнопку, которая вызывает функцию приветствия
greet_button = tk.Button(root, text="Поздороваться", command=greet)
greet_button.pack(pady=10)
# Создаем метку для отображения приветственного сообщения
greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=10)
# Запускаем главный цикл обработки событий
root.mainloop()

### Описание программы:
# - **Главное окно** создается с использованием `tk.Tk()` и получает заголовок "Приветствие".
# - **Метка** `instruction_label` сообщает пользователю, что нужно ввести свое имя.
# - **Текстовое поле** `name_entry` предоставляет пользователю возможность ввести свое имя.
# - **Кнопка** `greet_button` связана с функцией `greet`, которая считывает введенное имя и обновляет текст в `greeting_label`.
# - **Метка** `greeting_label` отображает приветственное сообщение после нажатия кнопки.