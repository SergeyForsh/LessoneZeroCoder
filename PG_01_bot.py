import telebot

# Замените 'YOUR_TOKEN' на токен вашего бота
TOKEN = '7856763609:AAEpR_zzqDfWl0SM-zkVll1upBeYjyl4jS4'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Подсчет количества символов в сообщении
    character_count = len(message.text)

    if message.text.lower() == "привет":
        bot.reply_to(message, f"Привет! Как я могу помочь? Вы отправили {character_count} символов.")
    elif message.text.lower() == "как дела?":
        bot.reply_to(message, f"Все отлично, спасибо! А у тебя как дела? Вы отправили {character_count} символов.")
    else:
        bot.reply_to(message,
                     f"Извини, я не понимаю. Попробуй спросить 'привет' или 'как дела?'. Вы отправили {character_count} символов.")


# Запуск бота
bot.polling()

# ### Изменения:
# 1. **Подсчет символов:** Я добавил строку `character_count = len(message.text)`,
# которая подсчитывает количество символов в сообщении пользователя.
# 2. **Информирование пользователя:** В ответах бота я включил информацию о количестве отправленных символов.
# Теперь бот будет сообщать пользователю, сколько символов он отправил в каждом сообщении!