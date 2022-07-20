import telebot, time, sqlite3
from telebot import types
# from mirea import parse as mirea_parse
from mipt import main as mipt_parse

with open('token.txt') as t:
    token = t.readline()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    global snils
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nПогнали тебя искать :3',
                           reply_markup=types.ReplyKeyboardRemove())
    try:
        connect = sqlite3.connect('users.db', check_same_thread=False)
        cursor = connect.cursor()
        cursor.execute(f"SELECT * FROM snils_id WHERE id = {message.chat.id}")
        data = cursor.fetchone()
        if data:
            snils = data[1]
            bot.send_message(message.chat.id, 'Эй, а я тебя помню!',
                                   reply_markup=types.ReplyKeyboardRemove())
            after_snils(message)
        else:
            enter_snils(message)
    except:
        enter_snils(message)

def enter_snils(mes):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton('Хочу')
    but2 = types.KeyboardButton('Не хочу')
    markup.add(but1, but2)
    mes = bot.send_message(mes.chat.id, 'Хочешь сохранить свой снилс, чтобы постоянно его не вводить?',
                           reply_markup=markup)
    bot.register_next_step_handler(mes, get_sinls)

def get_sinls(mes):
    global connect, cursor
    if mes.text == 'Хочу':
        mes = bot.send_message(mes.chat.id, 'Введите свой снилс в формате 11 цифр без разделителей',
                               reply_markup=types.ReplyKeyboardRemove())
        connect = sqlite3.connect('users.db', check_same_thread=False)
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS snils_id(
            id INTEGER,
            snils CHAR(14)
        )""")
        connect.commit()
        bot.register_next_step_handler(mes, snils_save)
    else:
        mes = bot.send_message(mes.chat.id, 'Введите свой снилс в формате 11 цифр без разделителей',
                               reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(mes, snils_not_save)

def snils_not_save(mes):
    global snils
    snils = mes.text
    if snils.isdigit():
        snils = f'{snils[:3]}-{snils[3:6]}-{snils[6:9]} {snils[9:]}'
    after_snils(mes)

def snils_save(mes):
    global snils
    snils = mes.text
    if snils.isdigit():
        snils = f'{snils[:3]}-{snils[3:6]}-{snils[6:9]} {snils[9:]}'
    cursor.execute(f"SELECT id FROM snils_id WHERE id = {mes.chat.id}")
    user_id = [mes.chat.id, snils]
    cursor.execute("INSERT INTO snils_id VALUES(?, ?);", user_id)
    connect.commit()
    after_snils(mes)

def after_snils(mes):
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
        but0 = types.KeyboardButton('Без критериев')
        but1 = types.KeyboardButton('Общий конкурс')
        but2 = types.KeyboardButton('Бюджет. Без вступительных испытаний')
        but3 = types.KeyboardButton('Целевая квота')
        but4 = types.KeyboardButton('Особая квота')
        but5 = types.KeyboardButton('В рамках квоты правительства РФ')
        but6 = types.KeyboardButton('Контракт (в т.ч. грант). БВИ')
        markup.add(but0, but1, but2, but3, but4, but5, but6)
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
    markup = None
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
    elif direction == '03.03.01 Прикладные математика и физика':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('ФРКТ Радиотехника и компьютерные технологии')
        but2 = types.KeyboardButton('ФРКТ Радиотехника и компьютерные технологии Иностранные граждане')
        but3 = types.KeyboardButton('ЛФИ Общая и прикладная физика')
        but4 = types.KeyboardButton('ЛФИ Общая и прикладная физика Иностранные граждане')
        but5 = types.KeyboardButton('ФАКТ Авиационные технологии')
        but6 = types.KeyboardButton('ФАКТ Геокосмические науки и технологии')
        but7 = types.KeyboardButton('ФАКТ Аэрокосмические технологии Иностранные граждане')
        but8 = types.KeyboardButton('ФЭФМ Физика перспективных технологий')
        but9 = types.KeyboardButton('ФЭФМ Физика перспективных технологий Иностранные граждане')
        but10 = types.KeyboardButton('ФПМИ Прикладная математика и компьютерные технологии')
        but11 = types.KeyboardButton('ФПМИ Прикладная математика и компьютерные технологии Иностранные граждане')
        but12 = types.KeyboardButton('ФБМФ Биофизика и биоинформатика')
        but13 = types.KeyboardButton('ФБМФ Биофизика и биоинформатика Иностранные граждане')
        but14 = types.KeyboardButton('ИНБИКСТ Конвергентные НБИК-технологии и мегасайенс')
        but15 = types.KeyboardButton('В рамках квоты правительства РФ (направление ПМФ)')
        but16 = types.KeyboardButton('ФБВТ Управление инновациями в бизнесе (ПМФ)')
        but17 = types.KeyboardButton('ФЭФМ Физика перспективных технологий Иностранные граждане')
        but18 = types.KeyboardButton('ФРКТ Радиотехника и компьютерные технологии (Предприятия Минпромторга)')
        but19 = types.KeyboardButton('ФАКТ Авиационные технологии (Предприятия Минпромторга)')
        but20 = types.KeyboardButton('ФАКТ Геокосмические науки и технологии (Предприятия Минпромторга)')
        but21 = types.KeyboardButton('ФАКТ Геокосмические науки и технологии (Предприятия Роскосмоса)')
        but22 = types.KeyboardButton('ФЭФМ Физика перспективных технологий (Предприятия Минпромторга)')
        but23 = types.KeyboardButton(
            'ФПМИ Прикладная математика и компьютерные технологии (ПМФ) (Предприятия Минпромторга)')
        but24 = types.KeyboardButton('ФБМФ Биофизика и биоинформатика (ГК Ростех)')
        markup.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10, but11, but12)
        markup.add(but13, but14, but15, but16, but17, but18, but19, but20, but21, but22, but23, but24)
    elif direction == '09.03.01 Информатика и вычислительная техника':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('ФАКТ Компьютерное моделирование')
        but2 = types.KeyboardButton('ФАКТ Компьютерное моделирование Иностранные граждане')
        but3 = types.KeyboardButton('ФПМИ Системное программирование и прикладная математика')
        but4 = types.KeyboardButton('ФПМИ Системное программирование и прикладная математика Иностранные граждане')
        but5 = types.KeyboardButton('В рамках квоты правительства РФ (направление ИВТ)')
        but6 = types.KeyboardButton('ФПМИ Прикладная математика и компьютерные технологии (ИВТ)')
        but7 = types.KeyboardButton('ВШПИ Программная инженерия (грантовые места, аналогичные бюджетным)')
        but8 = types.KeyboardButton('ФАКТ Компьютерное моделирование (Предприятия Роскосмоса)')
        but9 = types.KeyboardButton('ФАКТ Компьютерное моделирование (Предприятия Минпромторга)')
        but10 = types.KeyboardButton('ФПМИ Прикладная математика и компьютерные технологии (ИВТ) (АО «АТОМТЕХЭНЕРГО»)')
        markup.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10)
    elif direction == '11.03.04 Электроника и наноэлектроника':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('ФЭФМ Электроника и наноэлектроника')
        but2 = types.KeyboardButton('В рамках квоты Правительства РФ (направление ЭНЭ)')
        markup.add(but1, but2)
    elif direction == '16.03.01 Техническая физика':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('ФАКТ Техническая физика')
        but2 = types.KeyboardButton('В рамках квоты правительства РФ (направление ТФ)')
        markup.add(but1, but2)
    elif direction == '19.03.01 Биотехнология':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('ФБМФ Биотехнология')
        but2 = types.KeyboardButton('ФБМФ Биотехнология Иностранные граждане')
        but3 = types.KeyboardButton('Biomedical engineering for foreign citizens')
        but4 = types.KeyboardButton('В рамках квоты правительства РФ (направление БТ)')
        but5 = types.KeyboardButton('ФБВТ Управление инновациями в бизнесе (БТ)')
        markup.add(but1, but2, but3, but4, but5)
    elif direction == '27.04.03 Системный анализ и управление':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('ФАКТ Системный анализ и управление')
        but2 = types.KeyboardButton('В рамках квоты правительства РФ (направление САУ)')
        but3 = types.KeyboardButton('ФБВТ Управление инновациями в бизнесе (САУ)')
        but4 = types.KeyboardButton('ФАКТ Системный анализ и управление (Предприятия Минпромторга)')
        markup.add(but1, but2, but3, but4)
    elif direction == '10.05.01 Компьютерная безопасность':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton('Компьютерная безопасность')
        but2 = types.KeyboardButton('ФРКТ Компьютерная безопасность (Предприятия Минпромторга)')
        markup.add(but1, but2)
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
    time.sleep(3)
    bot.send_message(message.chat.id, 'Чтобы перезапустить бота - напиши /start')


# def mir(message):
#     global snils
#     t = message.text.upper()
#     print(snils, t)
#     info = mirea_parse(snils, t)


bot.polling(none_stop=True)
