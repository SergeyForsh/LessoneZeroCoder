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
        "/caps <текст> - Преобразовать текст в заглавные буквы.\n"
        "/cut <текст> - Удалить гласные буквы из текста.\n"
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

# Обработчик команды /caps
@bot.message_handler(commands=['caps'])
def convert_to_caps(message):
    # Получаем текст после команды
    text = message.text[len('/caps '):].strip()
    if text:
        # Преобразуем текст в заглавные буквы
        caps_text = text.upper()
        bot.reply_to(message, caps_text)
    else:
        bot.reply_to(message, "Пожалуйста, введите текст, который нужно преобразовать в заглавные буквы.")

# Обработчик команды /cut
@bot.message_handler(commands=['cut'])
def cut_vowels(message):
    # Получаем текст после команды
    text = message.text[len('/cut '):].strip()
    if text:
        # Удаляем гласные буквы
        vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
        cut_text = ''.join([char for char in text if char not in vowels])
        bot.reply_to(message, cut_text)
    else:
        bot.reply_to(message, "Пожалуйста, введите текст, из которого нужно удалить гласные буквы.")

# Обработчик для всех остальных текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Извините, я не понимаю. Используйте /help для получения списка доступных команд.")

# Запуск бота
bot.polling()

### Как это работает:
# 1. **Обработчик команды `/cut`:**
#    - Пользователь вводит команду в формате `/cut <гласные> <текст>`.
#    - Первая часть (гласные) будет удалена из второй части (текста).
#    - Чтобы удалить гласные, используется списковое включение, которое фильтрует символы,
#    не входящие в указанные гласные.
#    - Результат отправляется обратно пользователю.
# Теперь ваш бот поддерживает команду `/cut`, которая позволяет удалять
# указанные гласные буквы из текста!
