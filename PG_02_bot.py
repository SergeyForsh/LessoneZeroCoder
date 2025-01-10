import telebot

# Замените 'YOUR_TOKEN' на токен вашего бота
TOKEN = '7856763609:AAEpR_zzqDfWl0SM-zkVll1upBeYjyl4jS4'
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Я ваш бот-помощник. Используйте команду /help, чтобы узнать, что я могу сделать.")

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Я могу помочь вам с следующими командами:\n"
        "/start - Запустить бота и получить приветствие.\n"
        "/help - Получить информацию о командах.\n"
        "/perevorot <текст> - Перевернуть текст, который вы напишете.\n"
    )
    bot.reply_to(message, help_text)

# Обработчик команды /perevorot
@bot.message_handler(commands=['perevorot'])
def reverse_text(message):
    # Получаем текст после команды
    text = message.text[len('/perevorot '):].strip()
    if text:
        # Переворачиваем текст
        reversed_text = text[::-1]
        bot.reply_to(message, reversed_text)
    else:
        bot.reply_to(message, "Пожалуйста, введите текст, который нужно перевернуть.")

# Обработчик для всех остальных текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю. Используйте /help для получения списка доступных команд.")

# Запуск бота
bot.polling()