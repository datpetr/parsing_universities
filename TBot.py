import telebot
from telebot import types
import time
# from mirea import parse as mirea_parse
from mipt import main as mipt_parse

bot = telebot.TeleBot('5559239997:AAE2R5p7hH5OQzi--TcX0Pz-Gw0f_BelhkI')


@bot.message_handler(commands=['start'])
def start(message):
    mes = bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nВведите свой снилс',
                           reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(mes, get_sinls)


def get_sinls(mes):
    global snils
    snils = mes.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    u_mirea = types.KeyboardButton('МИРЭА')
    u_mipt = types.KeyboardButton('МФТИ')
    markup.add(u_mirea, u_mipt)
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
    if t == 'МФТИ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('Общий конкурс')
        but2 = types.KeyboardButton('Бюджет. Без вступительных испытаний')
        but3 = types.KeyboardButton('Целевая квота')
        but4 = types.KeyboardButton('Особая квота')
        but5 = types.KeyboardButton('В рамках квоты правительства РФ')
        but6 = types.KeyboardButton('Контракт (в т.ч. грант). БВИ')
        markup.add(but1, but2, but3, but4, but5, but6)
        mes = bot.send_message(message.chat.id, 'Условие поступления?', reply_markup=markup)
        bot.register_next_step_handler(mes, mip1)


def mip1(message):
    global admission_condition
    admission_condition = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('01.03.02 Прикладная математика и информатика')
    but2 = types.KeyboardButton('03.03.01 Прикладные математика и физика')
    but3 = types.KeyboardButton('09.03.01 Информатика и вычислительная техника')
    but4 = types.KeyboardButton('16.03.01 Техническая физика')
    but5 = types.KeyboardButton('19.03.01 Биотехнология')
    but6 = types.KeyboardButton('27.04.03 Системный анализ и управление')
    but7 = types.KeyboardButton('10.05.01 Компьютерная безопасность')
    but8 = types.KeyboardButton('11.03.04 Электроника и наноэлектроника')
    markup.add(but1, but2, but3, but4, but5, but6, but7, but8)
    mes = bot.send_message(message.chat.id, 'Направление?', reply_markup=markup)
    bot.register_next_step_handler(mes, mip2)


def mip2(message):
    global direction
    direction = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Бюджетное обучение')
    but2 = types.KeyboardButton('Контрактное обучение')
    markup.add(but1, but2)
    mes = bot.send_message(message.chat.id, 'Основа обучения?', reply_markup=markup)
    bot.register_next_step_handler(mes, mip3)


def mip3(message):
    global basis_of_learning, direction
    basis_of_learning = message.text
    if direction == '01.03.02 Прикладная математика и информатика':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('ФПМИ Прикладная математика и информатика')
        but2 = types.KeyboardButton('ФПМИ Экономика и ERP')
        but3 = types.KeyboardButton('ФПМИ Прикладная математика и информатика Иностранные граждане')
        but4 = types.KeyboardButton('Computer science for foreign citizens')
        but5 = types.KeyboardButton('Computer science')
        but6 = types.KeyboardButton('В рамках квоты правительства РФ (направление ПМИ)')
        but7 = types.KeyboardButton('ФПМИ Прикладная математика и информатика (Предприятия Минпромторга)')
        but8 = types.KeyboardButton('ФПМИ Прикладная математика и информатика (ПАО "ГАЗПРОМ НЕФТЬ")')
        markup.add(but1, but2, but3, but4, but5, but6, but7, but8)
        mes = bot.send_message(message.chat.id, 'Конкурсная группа?', reply_markup=markup)
        bot.register_next_step_handler(mes, mip4)


def mip4(message):
    global snils, admission_condition, direction, competitive_group, basis_of_learning
    competitive_group = message.text
    bot.send_message(message.chat.id, 'Произвожу поиск...', reply_markup=types.ReplyKeyboardRemove())
    user = mipt_parse(snils, admission_condition, direction, competitive_group, basis_of_learning)
    s1 = f'Номер в списке: {user["num"]}\nУровень приоритета: {user["priority"]}\n'
    s2 = f'Сумма баллов (с ИД): {user["sum_of_points_with_id"]}\nСогласие на зачисление: {user["education_document"]}'
    bot.send_message(message.chat.id, s1 + s2)
    time.sleep(5)
    bot.send_message(message.chat.id, 'Чтобы перезапустить бота - напиши /start')


# def mir(message):
#     global snils
#     t = message.text.upper()
#     print(snils, t)
#     info = mirea_parse(snils, t)


snils = 0
bot.polling(none_stop=True)
