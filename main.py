import telebot
from config import TOKEN
from bd import feather_drills, spiral_drills, discs_for_grinder

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_price = telebot.types.KeyboardButton(text='Выход на главное меню')
    button_price2 = telebot.types.KeyboardButton(text='Поиск товара')
    keyboard.add(button_price, button_price2)
    bot.send_message(chat_id,
                     'Добро пожаловать в бота для поиска описания и цены товаров. Также этот бот напишет, где находится интересующий товар и кинет на него ссылку.',
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Выход на главное меню')
def back_to_menu(message):
    welcome(message)


@bot.message_handler(func=lambda message: message.text == 'Поиск товара')
def buttons(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_price = telebot.types.KeyboardButton(text='Свёрла перьевые')
    button_price2 = telebot.types.KeyboardButton(text='Свёрла спиральные')
    button_price3 = telebot.types.KeyboardButton(text='Диски для болгарки')
    button_price5 = telebot.types.KeyboardButton(text='Выход на главное меню')
    keyboard.add(button_price, button_price2, button_price3, button_price5)
    bot.send_message(chat_id, 'Выберите товар из предложенного списка: ', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Свёрла перьевые')
def button(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_price = telebot.types.KeyboardButton(text='FIT FINCH INDUSTRIAL TOOLS')
    button_price2 = telebot.types.KeyboardButton(text='GEPARD')
    button_price3 = telebot.types.KeyboardButton(text='Выход на главное меню')
    keyboard.add(button_price, button_price2, button_price3)
    bot.send_message(chat_id, 'Выберите фирму/производитель товара: ', reply_markup=keyboard)

    @bot.message_handler(func=lambda message: message.text == 'FIT FINCH INDUSTRIAL TOOLS')
    def button(message):
        chat_id = message.chat.id
        with open('images/Набор перьевых свёрел Fit.webp', 'rb') as file:
            photo = file.read()
        bot.send_photo(chat_id, photo)
        a = feather_drills(1)
        bot.send_message(chat_id, a)
        bot.send_message(chat_id, 'Вот вся информация о данном товаре')

    @bot.message_handler(func=lambda message: message.text == 'GEPARD')
    def button(message):
        chat_id = message.chat.id
        with open('images/Набор перьевых свёрел Gipard.webp', 'rb') as file:
            photo = file.read()
        bot.send_photo(chat_id, photo)
        a = feather_drills(2)
        bot.send_message(chat_id, a)
        bot.send_message(chat_id, 'Вот вся информация о данном товаре')

    @bot.message_handler(func=lambda message: message.text == 'Tool Dreams')
    def button(message):
        chat_id = message.chat.id
        with open('images/Набор перьевых свёрел Tool Dreams.webp', 'rb') as file:
            photo = file.read()
        bot.send_photo(chat_id, photo)
        a = feather_drills(3)
        bot.send_message(chat_id, a)
        bot.send_message(chat_id, 'Вот вся информация о данном товаре')


@bot.message_handler(func=lambda message: message.text == 'Свёрла спиральные')
def button(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_price = telebot.types.KeyboardButton(text='По металлу')
    button_price2 = telebot.types.KeyboardButton(text='По дереву')
    button_price3 = telebot.types.KeyboardButton(text='Выход в главное меню')
    keyboard.add(button_price, button_price2, button_price3)
    bot.send_message(chat_id, 'Выберите тип:', reply_markup=keyboard)

    @bot.message_handler(func=lambda message: message.text == 'По металлу')
    def button(message):
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_price = telebot.types.KeyboardButton(text='Makita')
        button_price2 = telebot.types.KeyboardButton(text='GARWIN INDUSTRIAL')
        button_price3 = telebot.types.KeyboardButton(text='Bosch')
        keyboard.add(button_price, button_price2, button_price3)
        bot.send_message(chat_id, 'Выберите фирму:', reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text == 'Makita')
        def button(message):
            chat_id = message.chat.id
            with open('images/Makita свёрла.jpg', 'rb') as file:
                photo = file.read()
            bot.send_photo(chat_id, photo)
            a = spiral_drills(4)
            bot.send_message(chat_id, a)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')

            @bot.message_handler(func=lambda message: message.text == 'GARWIN INDUSTRIAL')
            def button(message):
                chat_id = message.chat.id
                with open('images/Свёрла спиральные Garwin.webp', 'rb') as file:
                    photo = file.read()
                bot.send_photo(chat_id, photo)
                a = spiral_drills(5)
                bot.send_message(chat_id, a)
                bot.send_message(chat_id, 'Вот вся информация о данном товаре')

            @bot.message_handler(func=lambda message: message.text == 'Bosch')
            def button(message):
                chat_id = message.chat.id
                with open('images/Спиральные свёрла bosch.webp', 'rb') as file:
                    photo = file.read()
                bot.send_photo(chat_id, photo)
                a = spiral_drills(6)
                bot.send_message(chat_id, a)
                bot.send_message(chat_id, 'Вот вся информация о данном товаре')


    @bot.message_handler(func=lambda message: message.text == 'По дереву')
    def button(message):
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_price = telebot.types.KeyboardButton(text='Patriot')
        button_price2 = telebot.types.KeyboardButton(text='Vira')
        button_price3 = telebot.types.KeyboardButton(text='Heller')
        button_price4 = telebot.types.KeyboardButton(text='Выход на главное меню')
        keyboard.add(button_price, button_price2, button_price3, button_price4)
        bot.send_message(chat_id, 'Выберите фирму:', reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text == 'Patriot')
        def button(message):
            chat_id = message.chat.id
            with open('images/Сверла спиарьные patriot.webp', 'rb') as file:
                photo = file.read()
            bot.send_photo(chat_id, photo)
            a = spiral_drills(1)
            bot.send_message(chat_id, a)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')

        @bot.message_handler(func=lambda message: message.text == 'Vira')
        def button(message):
            chat_id = message.chat.id
            with open('images/Сверла спиральные vira.webp', 'rb') as file:
                photo = file.read()
            bot.send_photo(chat_id, photo)
            a = spiral_drills(2)
            bot.send_message(chat_id, a)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')

        @bot.message_handler(func=lambda message: message.text == 'Heller')
        def button(message):
            chat_id = message.chat.id
            with open('images/Свёрла Heller.webp', 'rb') as file:
                photo = file.read()
            bot.send_photo(chat_id, photo)
            a = spiral_drills(3)
            bot.send_message(chat_id, a)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')


@bot.message_handler(func=lambda message: message.text == 'Диски для болгарки')
def button(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_price = telebot.types.KeyboardButton(text='Резка')
    button_price2 = telebot.types.KeyboardButton(text='Шлифовка')
    button_price3 = telebot.types.KeyboardButton(text='Выход на главное меню')
    keyboard.add(button_price, button_price2, button_price3)
    bot.send_message(chat_id, 'Выберите тип диска (для какого вида использования): ', reply_markup=keyboard)

    @bot.message_handler(func=lambda message: message.text == 'Резка')
    def button(message):
        chat_id = message.chat.id
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_price = telebot.types.KeyboardButton(text='LUGAABRASIV')
        button_price2 = telebot.types.KeyboardButton(text='ЗУБР')
        button_price3 = telebot.types.KeyboardButton(text='Выход на главное меню')
        keyboard.add(button_price, button_price2, button_price3)
        bot.send_message(chat_id, 'Выберите фирму: ', reply_markup=keyboard)


        @bot.message_handler(func=lambda message: message.text == 'LUGAABRASIV')
        def button(message):
            chat_id = message.chat.id
            with open('images/Диск для болгарки по металлу 125x1.2.png', 'rb') as file:
                photo = file.read()
            bot.send_photo(chat_id, photo)
            a = discs_for_grinder(1)
            bot.send_message(chat_id, a)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')

        @bot.message_handler(func=lambda message: message.text == 'ЗУБР')
        def button(message):
            chat_id = message.chat.id
            with open('images/Диск по металлу болгарка зубр.webp', 'rb') as file:
                photo = file.read()
            bot.send_photo(chat_id, photo)
            a = discs_for_grinder(2)
            bot.send_message(chat_id, a)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')


    @bot.message_handler(func=lambda message: message.text == 'Шлифовка')
    def button(message):
        chat_id = message.chat.id
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_price = telebot.types.KeyboardButton(text='Rexant')
        button_price2 = telebot.types.KeyboardButton(text='Vira')
        button_price3 = telebot.types.KeyboardButton(text='Выход на главное меню')
        keyboard.add(button_price, button_price2, button_price3)
        bot.send_message(chat_id, 'Выберите фирму: ', reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text == 'Rexant')
        def button(message):
            chat_id = message.chat.id
            with open('images/Лепестковый диск rexant + 1 фото.webp', 'rb') as file:
                photo = file.read()
                bot.send_photo(chat_id, photo)
            with open('images/+ 1 фото Rexant.webp', 'rb') as file:
                photo = file.read()
                bot.send_photo(chat_id, photo)
            a = discs_for_grinder(3)
            bot.send_message(chat_id, a)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')

        @bot.message_handler(func=lambda message: message.text == 'Vira')
        def button(message):
            chat_id = message.chat.id
            with open('images/1 фото Vira лепестковый диск.jpg', 'rb') as file:
                photo = file.read()
                bot.send_photo(chat_id, photo)
            with open('images/Диск лепестковый Vira + 1 фото.jpg', 'rb') as file:
                photo = file.read()
                bot.send_photo(chat_id, photo)
            a = discs_for_grinder(4)
            bot.send_message(chat_id, a)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()


