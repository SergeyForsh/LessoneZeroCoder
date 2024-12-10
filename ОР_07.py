import tkinter as tk
from tkinter import messagebox

def greet_user():
    name = name_entry.get()  # Получаем имя из поля ввода
    if name:  # Проверяем, что имя не пустое
        messagebox.showinfo("Приветствие", f"Привет, {name}!")
    else:
        messagebox.showwarning("Предупреждение", "Пожалуйста, введите ваше имя.")

# Создаем главное окно
root = tk.Tk()
root.title("Приветствие")

# Создаем метку
label = tk.Label(root, text="Введите ваше имя:")
label.pack(pady=10)

# Создаем поле ввода
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Создаем кнопку для приветствия
greet_button = tk.Button(root, text="Поздороваться", command=greet_user)
greet_button.pack(pady=20)

# Запускаем главный цикл
root.mainloop()