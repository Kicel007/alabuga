import telebot
import os.path
from telebot import types
import Svarka
bot = telebot.TeleBot('6697579021:AAG8uR2UKlbId9YkSRK-NTOPq_stWPIkepM')
active_sessions = dict()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Russian🇷🇺")
    btn2 = types.KeyboardButton("English🇬🇧")
    markup.add(btn1,btn2)
    active_sessions[message.chat.id] = 0
    bot.send_message(message.chat.id,
                     text="Добро пожаловать в бот для анализа качества сварки.Choose Language".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    global active_sessions
    if (message.text == "Загрузить фото"):
        hideBoard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Загрузите фото", reply_markup=hideBoard)
    if (message.text == "Upload Photo"):
        hideBoard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id, text="Upload photo", reply_markup=hideBoard)
    elif(message.text=="Russian🇷🇺"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Загрузить фото")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Выберите опцию", reply_markup=markup)
    elif (message.text == "English🇬🇧"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Upload Photo")
        markup.add(btn1)
        bot.send_message(message.chat.id, text="Choose option", reply_markup=markup)
    elif (message.text == "Узнать подробнее"):
        stt = 0
        try:
            hideBoard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            stt = active_sessions[str(message.chat.id)]
            if stt == "Bad Welding":
                bot.send_message(message.chat.id, text="""Bad Welding (плохая сварка):
                        - Проверьте качество сварочного материала.
                        - Убедитесь, что оборудование настроено правильно.
                        - Проверьте технику сварки и квалификацию сварщика.""", reply_markup=hideBoard)
            elif stt == "Crack":
                bot.send_message(message.chat.id, text="""Crack (трещина):
                        - Избегайте быстрого охлаждения сварочного шва.
                        - Правильно выбирайте метод сварки и материал.
                        - Проверьте совместимость материалов.""", reply_markup=hideBoard)
            elif stt == "Excess Reinforcement":
                bot.send_message(message.chat.id, text="""Excess Reinforcement (избыточное утолщение сварного шва):
                        - Контролируйте глубину проплавления при сварке.
                        - Используйте правильный размер электрода.
                        - Обратитесь к специалисту, если проблема повторяется.""", reply_markup=hideBoard)
            elif stt == "Good Welding":
                bot.send_message(message.chat.id, text="""Good Welding (качественная сварка)""", reply_markup=hideBoard)
            elif stt == "Posority":
                bot.send_message(message.chat.id, text="""Porosity (пористость):
                        - Избегайте загрязнений и влаги при сварке.
                        - Проверьте газовую среду вокруг сварочного шва.
                        - Убедитесь, что оборудование работает корректно.""", reply_markup=hideBoard)
            elif stt == "Spatters":
                bot.send_message(message.chat.id, text="""Spatters (брызги):
                        - Подберите правильный режим сварки.
                        - Очистите поверхность от загрязнений перед началом работы.
                        - Используйте антибрызговые средства или специальные настройки оборудования.""", reply_markup=hideBoard)
        except:
            bot.send_message(message.chat.id, text="Вы не выбрали опцию")
    elif (message.text =="Find out more"):
        stt = 0
        try:
            hideBoard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            stt = active_sessions[str(message.chat.id)]
            if stt == "Bad Welding":
                bot.send_message(message.chat.id, text="""Bad Welding:
                                - Check the quality of the welding material.
                                - Make sure the equipment is set up correctly.
                                - Check the welding technique and the welder's experience level.""", reply_markup=hideBoard)
            elif stt == "Crack":
                bot.send_message(message.chat.id, text="""Crack:
                                - Avoid fast cooling of the weld.
                                - Select the right welding method and material.
                                - Check compatibility of materials""",reply_markup=hideBoard)
            elif stt == "Excess Reinforcement":
                bot.send_message(message.chat.id, text="""Excess Reinforcement:
                                - Control the depth of penetration when welding.
                                - Use the correct electrode size.
                                - Consult a specialist if the problem repeats""", reply_markup=hideBoard)
            elif stt == "Good Welding":
                bot.send_message(message.chat.id, text="High-quality reconciliation", reply_markup=hideBoard)
            elif stt == "Posority":
                bot.send_message(message.chat.id, text="""Porosity:
                                - Avoid contaminants and moisture when welding.
                                - Check the gas environment around the weld.
                                - Make sure the equipment works properly.""", reply_markup=hideBoard)
            elif stt == "Spatters":
                bot.send_message(message.chat.id, text="""Spatters:
                                - Select the correct welding mode.
                                - Clean the surface from contaminants before starting work.
                                - Use anti-spatter agents or special equipment settings.""",
                                 reply_markup=hideBoard)
        except:
            bot.send_message(message.chat.id, text="Вы не выбрали опцию")
    else:
        bot.send_message(message.chat.id, text="Неверный формат сообщения")


@bot.message_handler(content_types=['photo'])
def photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    sss = str(message.chat.id) + ".jpg"
    with open(sss, 'wb') as new_file:
        new_file.write(downloaded_file)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Find out more")
    btn2 = types.KeyboardButton("Узнать больше")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Узнать больше/Find out more", reply_markup=markup)
    tx=Svarka.get_defect(sss)
    active_sessions[str(message.chat.id)]=tx
bot.polling(none_stop=True)
