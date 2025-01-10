import telebot
from openai import OpenAI
from gtts import gTTS
import os

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

# Функция для преобразования текста в речь
def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='ru')  # Убедитесь, что язык соответствует вашему тексту
    tts.save(filename)

# Обработчик сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Инициализация сообщений
    messages = [{"role": "user", "content": message.text}]

    # Получение ответа от нейросети
    response = chat_with_ai(messages)

    # Преобразование ответа в голосовое сообщение
    audio_filename = 'response.mp3'
    text_to_speech(response, audio_filename)

    # Отправка голосового сообщения пользователю
    with open(audio_filename, 'rb') as audio_file:
        bot.send_voice(message.chat.id, audio_file)

    # Удаление временного файла
    os.remove(audio_filename)

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling()