import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('7676922385:AAEBry6haCat8uRJehr0CLDeOAa1sPfKM80')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе о твоих делах')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id, ))
    reminder_thread.start()

@bot.message_handler(commands=['fakt'])
def fakt_message(message):
    list = ['сделать зарядку', 'умыться', 'позавтракать']
    random_fakt = random.choice(list)
    bot.reply_to(message, f'Лови факт о выполненых делах: {random_fakt}')

def send_reminders(chat_id):
    first_rem = '09:00'
    second_rem = '15:30'
    end_rem = '18:00'
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, 'Напоминание - сделай дело')
            time.sleep(61)
        time.sleep(1)
bot.polling(none_stop=True)