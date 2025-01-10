import telebot
from openai import OpenAI

# Инициализация клиента OpenAI
client = OpenAI(
    api_key="sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I",
    base_url="https://api.proxyapi.ru/openai/v1",
)
# Инициализация бота
TOKEN = '7856763609:AAEpR_zzqDfWl0SM-zkVll1upBeYjyl4jS4'  # Замените на ваш токен бота
bot = telebot.TeleBot(TOKEN)

# Функция для общения с нейросетью
def chat_with_ai(messages):
    # Получение ответа от нейросети
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )
    # Получение и возврат ответа
    response_content = chat_completion.choices[0].message.content
    return response_content

# Обработчик сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Инициализация сообщений
    messages = [{"role": "user", "content": message.text}]

    # Получение ответа от нейросети
    response = chat_with_ai(messages)

    # Отправка ответа пользователю
    bot.reply_to(message, response)

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling()