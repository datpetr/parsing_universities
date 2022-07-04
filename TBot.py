import telebot
from telebot import types
from mirea import parse as mirea_parse

bot = telebot.TeleBot('5559239997:AAE2R5p7hH5OQzi--TcX0Pz-Gw0f_BelhkI')

@bot.message_handler(commands=['start'])
def start(message):
    mes = bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nВведите свой снилс')
    bot.register_next_step_handler(mes, get_sinls)
def get_sinls(mes):
    global snils
    snils = mes.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    u_mirea = types.KeyboardButton('МИРЭА')
    markup.add(u_mirea)
    bot.send_message(mes.chat.id, 'Выберите ВУЗ, списки которого вы хотите посмотреть', reply_markup=markup)

@bot.message_handler(content_types='text')
def text(message):
    global snils
    t = message.text
    if t == 'МИРЭА':
        mes = bot.send_message(message.chat.id, 'Какое направление?', reply_markup=types.ReplyKeyboardRemove())
        with open('mirea.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f)
        bot.register_next_step_handler(mes, mir)
def mir(message):
    global snils
    t = message.text.upper()
    print(snils, t)
    info = mirea_parse(snils, t)




snils = 0
bot.polling(none_stop=True)