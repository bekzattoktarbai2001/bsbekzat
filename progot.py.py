import telebot
from telebot import types
# токен-бота
bot = telebot.TeleBot('1469655161:AAGcnWTTX8lXQ5EHuUNcauSHUnijItM0FwE')

# если /help, /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Сәлем! "
                     + message.from_user.first_name
                     + ", Бұл ботта фото,видео монтажға арналған қосымшамен және камераға арналған қосымшалармен танысасыз!!!",
                     reply_markup=markup_menu)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_1 = types.KeyboardButton('Photo 1-5')
btn_2 = types.KeyboardButton('Video 6-10')
btn_3 = types.KeyboardButton('Camera 11-15')
markup_menu.add(btn_1, btn_2, btn_3)


Camera1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_a1 = types.KeyboardButton('Photo 1')
btn_a2 = types.KeyboardButton('Photo 2')
btn_a3 = types.KeyboardButton('Photo 3')
btn_a4 = types.KeyboardButton('Photo 4')
btn_a5 = types.KeyboardButton('Photo 5')
btn_a6 = types.KeyboardButton('В меню')
Camera1.add(btn_a1, btn_a2, btn_a3, btn_a4, btn_a5, btn_a6)

Camera2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_a7 = types.KeyboardButton('Video 6')
btn_a8 = types.KeyboardButton('Video 7')
btn_a9 = types.KeyboardButton('Video 8')
btn_a10 = types.KeyboardButton('Video 9')
btn_a11 = types.KeyboardButton('Video 10')
btn_a12 = types.KeyboardButton('В меню')
Camera2.add(btn_a7, btn_a8, btn_a9, btn_a10, btn_a11, btn_a12)

Camera3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn_a13 = types.KeyboardButton('Camera 11')
btn_a14 = types.KeyboardButton('Camera 12')
btn_a15 = types.KeyboardButton('Camera 13')
btn_a16 = types.KeyboardButton('Camera 14')
btn_a17 = types.KeyboardButton('Camera 15')
btn_a18 = types.KeyboardButton('В меню')
Camera3.add(btn_a13, btn_a14, btn_a15, btn_a16,btn_a17, btn_a18)
vmenyu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_naz5 = types.KeyboardButton('В меню')
vmenyu.add(btn_naz5)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "В меню":
        bot.reply_to(message, "Назад", reply_markup=markup_menu)
    if message.text == "Photo 1-5":
        bot.reply_to(message, "Выберите номер Photo от 1-5", reply_markup=Camera1)
    if message.text == "Video 6-10":
        bot.reply_to(message, "Выберите номер Video от 6-10", reply_markup=Camera2)
    if message.text == "Camera 11-15":
        bot.reply_to(message, "Выберите номер Camera от 11-15", reply_markup=Camera3)
    if message.text == "Photo 1":
        bot.reply_to(message,
                     """https://ru.wikipedia.org/wiki/Adobe_Photoshop_Lightroom""",
                     reply_markup=Camera1)
    if message.text == "Photo 2":
        bot.reply_to(message, """https://ru.wikipedia.org/wiki/Vsco""",
                     reply_markup=Camera1)
    if message.text == "Photo 3":
        bot.reply_to(message,
                     """https://ru.wikipedia.org/wiki/Snapseed""",
                     reply_markup=Camera1)
    if message.text == "Photo 4":
        bot.reply_to(message, """https://en.wikipedia.org/wiki/PicsArt""",
                     reply_markup=Camera1)
    if message.text == "Photo 5":
        bot.reply_to(message,
                     """https://ru.wikipedia.org/wiki/Adobe_Photoshop""",
                     reply_markup=Camera1)
    if message.text == "Video 6":
        bot.reply_to(message,
                     """https://ru.wikipedia.org/wiki/IMovie""",
                     reply_markup=Camera2)
    if message.text == "Video 7":
        bot.reply_to(message,
                     """https://apps.apple.com/ru/app/videoleap-%D0%BC%D0%BE%D0%BD%D1%82%D0%B0%D0%B6-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE/id1255135442""",
                     reply_markup=Camera2)
    if message.text == "Video 8":
        bot.reply_to(message,
                     """https://en.wikipedia.org/wiki/Stop_motion""",
                     reply_markup=Camera2)
    if message.text == "Video 9":
        bot.reply_to(message,
                     """https://lomotif.com/""",
                     reply_markup=Camera2)
    if message.text == "Video 10":
        bot.reply_to(message,
                     """https://apps.apple.com/ru/app/videoleap-%D0%BC%D0%BE%D0%BD%D1%82%D0%B0%D0%B6-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE/id1255135442""",
                     reply_markup=Camera2)
    if message.text == "Camera 11":
        bot.reply_to(message, """https://www.lomography.com/""",
                     reply_markup=Camera3)
    if message.text == "Camera 12":
        bot.reply_to(message, """https://play.google.com/store/apps/details?id=photoeditor.oldfilter.retroeffect.vintagecamera&hl=en_US&gl=US""",
                     reply_markup=Camera3)
    if message.text == "Camera 13":
        bot.reply_to(message, """https://apkpure.com/retro-film-photo-filter-for-old-fashioned-film/com.optimicode.retrofilm""",
                     reply_markup=Camera3)
    if message.text == "Camera 14":
        bot.reply_to(message, """https://apps.apple.com/ru/app/nomo-point-and-shoot/id1362548649""",
                     reply_markup =Camera3)
    if message.text == "Camera 15":
        bot.reply_to(message, """https://apps.apple.com/ru/app/slo-mo-video-%D1%80%D0%B5%D0%B4%D0%B0%D0%BA%D1%82%D0%BE%D1%80-%D0%B7%D0%B0%D0%BC%D0%B5%D0%B4%D0%BB%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE-%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE-%D0%B4%D0%BB%D1%8F-youtube/id1056995900""",
                     reply_markup=Camera3)
bot.polling()