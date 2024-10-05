from turtledemo.forest import start
from unittest import enterModuleContext

import telebot
from telebot import types
bot = telebot.TeleBot('7870427080:AAHQ8LMDZU567NhtlB8xi0dGrQP6wP2u90Y')

@bot.message_handler(commands=['start'])
def start(message):
    txt = 'Здравствуйте! Давайте я провожу вас по стране буквы Н и расскажу о ней.'

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    Button1 = types.KeyboardButton('Перейти к рассказу')
    Button2 = types.KeyboardButton('Перейти к словарю')

    markup.add(Button1, Button2)

    bot.send_message(message.chat.id, txt, reply_markup=markup)

@bot.message_handler(content_types=['text'])
def sus(message):
    if message.text == 'Перейти к рассказу':
        txt = 'С нимбом на голове и наушниками, через которые раздавались волшебные звуки,'\
               ' я шёл, окруженный горами, в сторону солнца. '\
               'Вокруг меня сновали нейтроны, невидимые частицы, пронизывающие все вокруг. '\
               'Под ногами хрустел наст, искрящийся под лучами солнца. '\
               'Повсюду мелькали носы - загадочные существа, которые, казалось, следили за каждым моим движением. '
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        Button1 = types.KeyboardButton('Нимб')
        Button2 = types.KeyboardButton('Наушники')
        Button3 = types.KeyboardButton('Нейтроны')
        Button4 = types.KeyboardButton('Наст')
        Button5 = types.KeyboardButton('Носы')
        Button6 = types.KeyboardButton('Читать дальше')
        Button7 = types.KeyboardButton('Вернуться назад')

        markup.add(Button1, Button2, Button3, Button4, Button5, Button6, Button7)

        bot.send_message(message.chat.id, txt, reply_markup=markup)

    elif message.text == 'Читать дальше':
        txt = 'Каждый шаг приближал меня к тайнам этого необычного мира. '\
               'В небе парили прекрасные нимфы, создавая вокруг себя ореол мистической красоты. '\
               'И даже воздух, которым я дышал, был пропитан ароматом нитрогениума - '\
                'таинственного элемента, придающего этой стране ее неповторимый облик. '

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        Button1 = types.KeyboardButton('Нимфы')
        Button2 = types.KeyboardButton('Нитрогениум')
        Button3 = types.KeyboardButton('Вернуться назад')
        Button4 = types.KeyboardButton('Читать далее')

        markup.add(Button1, Button2, Button3, Button4)

        bot.send_message(message.chat.id, txt, reply_markup=markup)

    elif message.text == 'Читать далее':
        txt = 'Очарованный, я продолжал свое путешествие, открывая для себя все '\
               'новые и новые чудеса этой удивительной страны Н. '\
               'Каждый предмет, каждое явление здесь было наполнено магией и тайной, '\
                'побуждая меня исследовать и познавать этот удивительный мир.'

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

        Button1 = types.KeyboardButton('Вернуться назад')

        markup.add(Button1)

        bot.send_message(message.chat.id, txt, reply_markup=markup)

    elif message.text == 'Перейти к словарю':
        txt = 'Ознакомьтесь с небольшим словарем из страны Н.'

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        Button1 = types.KeyboardButton('Нимб')
        Button2 = types.KeyboardButton('Наушники')
        Button3 = types.KeyboardButton('Нейтроны')
        Button4 = types.KeyboardButton('Наст')
        Button5 = types.KeyboardButton('Носы')
        Button6 = types.KeyboardButton('Нимфы')
        Button7 = types.KeyboardButton('Нитрогениум')
        Button8 = types.KeyboardButton('Вернуться назад')

        markup.add(Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8)

        bot.send_message(message.chat.id, txt, reply_markup=markup)

    elif message.text == 'Вернуться назад':
        txt = 'Здравствуйте! Давайте я провожу вас по стране буквы Н и расскажу о ней.'

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

        Button1 = types.KeyboardButton('Перейти к рассказу')
        Button2 = types.KeyboardButton('Перейти к словарю')
        markup.add(Button1, Button2)

        bot.send_message(message.chat.id, txt, reply_markup=markup)

    elif message.text == 'Нимб':
        txt = 'Нимб - условное обозначение сияния вокруг головы '\
               '(наравне с лучезарным венцом), символизирующее святость.'

        Ni = open('0ac8b622-6631-4037-b0d5-ae259d6b9522.jpg', 'rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(Ni)])

    elif message.text == 'Наушники':
        txt = 'Наушники — устройство для персонального прослушивания звуковой информации. '\
               'Они представляют собой пару небольших головных телефонов или блока наушника, '\
               'надеваемых на голову или вставляемых прямо в ушные каналы.'

        Ni = open('02274d29-c22a-42a2-ac9d-f869f73bea42.jpg', 'rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(Ni)])

    elif message.text == 'Нейтроны':
        txt = 'Нейтроны - частица без заряда с относительной массой (1). Находится в ядре атома.'

        Ni = open('88b85664-332a-4039-9920-e2eafe572c3e.jpg', 'rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(Ni)])

    elif message.text == 'Наст':
        txt = 'Наст — это плотная корка снега на поверхности или в более глубоких слоях снежного покрова. '\
               'Образуется в результате подтаивания и последующего замерзания снега либо в результате '\
               'ветрового уплотнения (ветровой наст).'

        Ni = open('2d6c0eca-baae-4ea4-8d41-35dedd69cc49.jpg', 'rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(Ni)])

    elif message.text == 'Носы':
        txt = 'Нос - 1. Орган обоняния, а также часть лица, морды, расположенная надо ртом и являющаяся'\
               ' наружной частью органа обоняния; 2. Небольшие существа, улетевшие от людей,'\
               'которые сильно их задирали (в нашем рассказе)'

        Ni = open('8601c2c8-1e29-4730-be76-f30f13618f35.jpg', 'rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(Ni)])

    elif message.text == 'Нимфы':
        txt = 'Нимфы - божества природы в древнегреческой мифологии в виде девушек, '\
               'олицетворяющих различные живительные и плодоносные силы Земли, природные объекты и явления.'

        Ni = open('064470a3-c2c5-4f43-a370-a2fb51477103.jpg', 'rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(Ni)])

    elif message.text == 'Нитрогениум':
        txt = 'Нитрогениум(азот) - химический элемент 15-й группы второго периода '\
               'периодической системы Д. И. Менделеева с атомным номером 7.'

        Ni = open('5188466982473817817.jpg', 'rb')

        bot.send_message(message.chat.id, txt)
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(Ni)])


bot.polling(non_stop=True)

