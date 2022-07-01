import telebot
from telebot import types
from mirea import parse as mirea_parse

bot = telebot.TeleBot('5559239997:AAE2R5p7hH5OQzi--TcX0Pz-Gw0f_BelhkI')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введите снилс')

@bot.message_handler(content_types='text')
def text(message):
    t = message.text
    if t.isdigit():
        snils = message.text
    if t == 'МИРЭА':
        u_mirea1 = '01.03.02 Прикладная математика и информатика (ИИИ)'
        bot.send_message(message.chat.id, 'Какое направление?')
        mir(message, snils)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    u_mirea = types.KeyboardButton('МИРЭА')
    markup.add(u_mirea)
    bot.send_message(message.chat.id, 'Выберите ВУЗ, списки которого вы хотите посмотреть', reply_markup=markup)

def mir(message, snils):
    bot.send_message(message.chat.id, '')

bot.polling(none_stop=True)