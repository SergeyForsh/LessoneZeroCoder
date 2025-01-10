from openai import OpenAI

# Инициализация клиента OpenAI
client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
    base_url="https://api.proxyapi.ru/openai/v1",
)

# Функция для общения с нейросетью
def chat_with_ai():
    print("Вы можете начать общаться с нейросетью. Для выхода введите 'exit'.")

    # Инициализация сообщений
    messages = []

    while True:
        user_input = input("Вы: ")

        if user_input.lower() == 'exit':
            print("Выход из чата.")
            break

        # Добавление сообщения пользователя в историю
        messages.append({"role": "user", "content": user_input})

        # Получение ответа от нейросети
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages
        )
        # Получение и вывод ответа
        response_content = chat_completion.choices[0].message.content
        print("AI:", response_content)

        # Добавление ответа нейросети в историю
        messages.append({"role": "assistant", "content": response_content})

# Запуск функции общения с нейросетью
if __name__ == "__main__":
    chat_with_ai()




    ### Описание кода:
#     1. ** Импорт и инициализация
#     **: Вы импортируете нужные библиотеки и инициализируете клиента OpenAI с вашим API ключом
#     и базовым URL.
#     2. ** Функция `chat_with_ai`
#     **: Создается функция, которая обрабатывает ввод пользователя и отправляет запросы к нейросети.
#     3. ** Цикл общения
#     **: Внутри функции `chat_with_ai` реализован бесконечный цикл, в котором:
#     - Запрашивается ввод пользователя.
#     - Если пользователь вводит `exit`, программа завершается.
#     - Ввод пользователя добавляется в историю сообщений.
#     - Отправляется запрос к нейросети, и полученный ответ выводится на экран.
#     - Ответ нейросети также добавляется в историю сообщений для контекста будущих запросов.
#     4. ** Запуск **: В самом конце скрипта проверяется, если он запущен как основной модуль,
#     и вызывается функция `chat_with_ai`.
#     Теперь, запустив этот код, вы сможете общаться с нейросетью в консоли.
