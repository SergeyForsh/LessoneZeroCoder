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
        messages.append({"role": "user", "content": response_content})
        # Определите переменную user_message
        user_message = "Ваше сообщение здесь"
        # Замените текст на нужный
        # Теперь вы можете добавить сообщение в список
        messages.append({"role": "user", "content": user_message})
# Запуск функции общения с нейросетью
if __name__ == "__main__":
    chat_with_ai()