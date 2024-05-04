"""
Основной модуль программы, содержит логику работы бота, взаимодействия его с
базой данных посредством нажатия на кнопки клавиатур
"""
import telebot
from config import TOKEN
from bd import feather_drills, spiral_drills, discs_for_grinder

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    """
    Начальные действия бота по команде start

    Бот отправляет приветственное письмо пользователю и объясняет ему, что он умеет делать и для чего нужен.
    Пользователю также на клавиатуре выдаётся 2 кнопки: 'Выход на главное меню', 'Поиск товара'.
    """
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
    """
    Вызов кнопки возврата на главное меню.

    Позволяет пользователю вернуться в любой момент работы бота в самое начало его (главное меню).
    """
    welcome(message)


@bot.message_handler(func=lambda message: message.text == 'Поиск товара')
def main_buttons(message):
    """
    Действия бота при нажатии на кнопку "Поиск товара" пользователем.

    При нажатии на кнопку "Поиск товара", пользователю выдаётся 3 новых кнопки на клавиатуре: "Свёрла перьевые", "Свёрла спиральные", "Диски для болгарки".
    И одна кнопка остаётся всегда - "Выход на главное меню". Новые кнопки нужны для того, чтобы выбрать вид строительного товара.
    """
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_price = telebot.types.KeyboardButton(text='Свёрла перьевые')
    button_price2 = telebot.types.KeyboardButton(text='Свёрла спиральные')
    button_price3 = telebot.types.KeyboardButton(text='Диски для болгарки')
    button_price5 = telebot.types.KeyboardButton(text='Выход на главное меню')
    keyboard.add(button_price, button_price2, button_price3, button_price5)
    bot.send_message(chat_id, 'Выберите товар из предложенного списка: ', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Свёрла перьевые')
def buttons_of_firm_of_feather_drills(message):
    """
    Действия бота при нажатии на кнопку "Свёрла перьевые" пользователем.

    При нажатии на кнопку "Свёрла перьевые", пользователю выдаётся 3 новых кнопки на клавиатуре:
    "FIT FINCH INDUSTRIAL TOOLS", "GEPARD", "Tool Dreams" - это фирмы производителей выбранного ранее вида товаров.
    """
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_price = telebot.types.KeyboardButton(text='FIT FINCH INDUSTRIAL TOOLS')
    button_price2 = telebot.types.KeyboardButton(text='GEPARD')
    button_price3 = telebot.types.KeyboardButton(text='Tool Dreams')
    button_price4 = telebot.types.KeyboardButton(text='Выход на главное меню')
    keyboard.add(button_price, button_price2, button_price3, button_price4)
    bot.send_message(chat_id, 'Выберите фирму/производитель товара: ', reply_markup=keyboard)

    @bot.message_handler(func=lambda message: message.text == 'FIT FINCH INDUSTRIAL TOOLS')
    def fit_finch_company_product_information(message):
        chat_id = message.chat.id
        with open('images/Набор перьевых свёрел Fit.webp', 'rb') as file:
            photo = file.read()
        bot.send_photo(chat_id, photo)
        information_database = feather_drills(1)
        bot.send_message(chat_id, information_database)
        bot.send_message(chat_id, 'Вот вся информация о данном товаре')

    """
    Действия бота при нажатии на кнопку "FIT FINCH INDUSTRIAL TOOLS" - фирма выбранного ранее товара.

    Бот при нажатии на данную кнопку высылает фото данного товара, которое открывается по ссылке из памяти компьютера.
    А потом из базы данных "favorable_prices" и таблицы "Feather_drills" скидывает пользователю описание, ссылку на этот
    товар (в каком магазине купить его и по какой цене).
    """

    @bot.message_handler(func=lambda message: message.text == 'GEPARD')
    def gepard_company_product_information(message):
        """
        Действия бота при нажатии на кнопку "GEPARD" - фирма выбранного ранее товара.

        Бот при нажатии на данную кнопку высылает фото данного товара, которое открывается по ссылке из памяти компьютера.
        А потом из базы данных "favorable_prices" и таблицы "Feather_drills" скидывает пользователю описание, ссылку на этот
        товар (в каком магазине купить его и по какой цене).
        """
        chat_id = message.chat.id
        with open('images/Набор перьевых свёрел Gipard.webp', 'rb') as file:
            photo = file.read()
        bot.send_photo(chat_id, photo)
        information_database = feather_drills(2)
        bot.send_message(chat_id, information_database)
        bot.send_message(chat_id, 'Вот вся информация о данном товаре')

    @bot.message_handler(func=lambda message: message.text == 'Tool Dreams')
    def tool_dreams_company_product_information(message):
        """
        Действия бота при нажатии на кнопку "Tool Dreams" - фирма выбранного ранее товара.

        Бот при нажатии на данную кнопку высылает фото данного товара, которое открывается по ссылке из памяти компьютера.
        А потом из базы данных "favorable_prices" и таблицы "Feather_drills" скидывает пользователю описание, ссылку на этот
        товар (в каком магазине купить его и по какой цене).
        """

        chat_id = message.chat.id
        with open('images/Набор перьевых свёрел Tool Dreams.webp', 'rb') as file:
            photo = file.read()
        bot.send_photo(chat_id, photo)
        information_database = feather_drills(3)
        bot.send_message(chat_id, information_database)
        bot.send_message(chat_id, 'Вот вся информация о данном товаре')


@bot.message_handler(func=lambda message: message.text == 'Свёрла спиральные')
def buttons_of_special_spiral_drills(message):
    """
    Действия бота при нажатии на кнопку "Свёрла спиральные" пользователем.

    При нажатии на кнопку "Свёрла спиральные", пользователю выдаётся 2 новых кнопки на клавиатуре:
    "По металлу", "По дереву" - это кнопки, с помощью которых можно выбрать вид набора свёрел (товара),
    по какому материалу будет производится сверление.
    """
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_price = telebot.types.KeyboardButton(text='По металлу')
    button_price2 = telebot.types.KeyboardButton(text='По дереву')
    button_price3 = telebot.types.KeyboardButton(text='Выход на главное меню')
    keyboard.add(button_price, button_price2, button_price3)
    bot.send_message(chat_id, 'Выберите тип:', reply_markup=keyboard)

    @bot.message_handler(func=lambda message: message.text == 'По металлу')
    def buttons_of_metal_of_firm_of_spiral_drills(message):
        """
        Действия бота при нажатии на кнопку "По металлу" - вид материала по которому будет производиться сверление.

        При нажатии на кнопку "По металлу", пользователю выдаётся 3 новых кнопки на клавиатуре:
        "Makita", "GARWIN INDUSTRIAL", "Bosch" - это фирмы производителей выбранного ранее вида товаров.
        """
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_price = telebot.types.KeyboardButton(text='Makita')
        button_price2 = telebot.types.KeyboardButton(text='GARWIN INDUSTRIAL')
        button_price3 = telebot.types.KeyboardButton(text='Bosch')
        keyboard.add(button_price, button_price2, button_price3)
        bot.send_message(chat_id, 'Выберите фирму:', reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text == 'Makita')
        def makita_company_product_information(message):
            """
            Действия бота при нажатии на кнопку "Makita" - фирма выбранного ранее товара.

            Бот при нажатии на данную кнопку высылает фото данного товара, которое открывается по ссылке из памяти компьютера.
            А потом из базы данных "favorable_prices" и таблицы "Spiral_drills" скидывает пользователю описание, ссылку на этот
            товар (в каком магазине купить его и по какой цене).
            """
            chat_id = message.chat.id
            with open('images/Makita свёрла.jpg', 'rb') as file:
                photo = file.read()
            bot.send_photo(chat_id, photo)
            information_database = spiral_drills(4)
            bot.send_message(chat_id, information_database)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')

            @bot.message_handler(func=lambda message: message.text == 'GARWIN INDUSTRIAL')
            def garwin_company_product_information(message):
                """
                Действия бота при нажатии на кнопку "GARWIN INDUSTRIAL" - фирма выбранного ранее товара.

                Бот при нажатии на данную кнопку высылает фото данного товара, которое открывается по ссылке из памяти компьютера.
                А потом из базы данных "favorable_prices" и таблицы "Spiral_drills" скидывает пользователю описание, ссылку на этот
                товар (в каком магазине купить его и по какой цене).
                """
                chat_id = message.chat.id
                with open('images/Свёрла спиральные Garwin.webp', 'rb') as file:
                    photo = file.read()
                bot.send_photo(chat_id, photo)
                information_database = spiral_drills(5)
                bot.send_message(chat_id, information_database)
                bot.send_message(chat_id, 'Вот вся информация о данном товаре')

            @bot.message_handler(func=lambda message: message.text == 'Bosch')
            def bosch_company_product_information(message):
                """
                Действия бота при нажатии на кнопку "Bosch" - фирма выбранного ранее товара.

                Бот при нажатии на данную кнопку высылает фото данного товара, которое открывается по ссылке из памяти компьютера.
                А потом из базы данных "favorable_prices" и таблицы "Spiral_drills" скидывает пользователю описание, ссылку на этот
                товар (в каком магазине купить его и по какой цене).
                """

                chat_id = message.chat.id
                with open('images/Спиральные свёрла bosch.webp', 'rb') as file:
                    photo = file.read()
                bot.send_photo(chat_id, photo)
                information_database = spiral_drills(6)
                bot.send_message(chat_id, information_database)
                bot.send_message(chat_id, 'Вот вся информация о данном товаре')

    @bot.message_handler(func=lambda message: message.text == 'По дереву')
    def buttons_of_wood_of_firm_of_spiral_drills(message):
        """
        Действия бота при нажатии на кнопку "По дереву" - вид материала по которому будет производиться сверление.

        При нажатии на кнопку "По дереву", пользователю выдаётся 3 новых кнопки на клавиатуре:
        "Patriot", "Vira", "Heller" - это фирмы производителей выбранного ранее вида товаров.
        """
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_price = telebot.types.KeyboardButton(text='Patriot')
        button_price2 = telebot.types.KeyboardButton(text='Vira')
        button_price3 = telebot.types.KeyboardButton(text='Heller')
        button_price4 = telebot.types.KeyboardButton(text='Выход на главное меню')
        keyboard.add(button_price, button_price2, button_price3, button_price4)
        bot.send_message(chat_id, 'Выберите фирму:', reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text == 'Patriot')
        def patriot_company_product_information(message):
            """
            Действия бота при нажатии на кнопку "Patriot" - фирма выбранного ранее товара.

            Бот при нажатии на данную кнопку высылает фото данного товара, которое открывается по ссылке из памяти компьютера.
            А потом из базы данных "favorable_prices" и таблицы "Spiral_drills" скидывает пользователю описание, ссылку на этот
            товар (в каком магазине купить его и по какой цене).
            """

            chat_id = message.chat.id
            with open('images/Сверла спиарьные patriot.webp', 'rb') as file:
                photo = file.read()
            bot.send_photo(chat_id, photo)
            information_database = spiral_drills(1)
            bot.send_message(chat_id, information_database)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')

        @bot.message_handler(func=lambda message: message.text == 'Vira')
        def vira_company_product_information(message):
            """
            Действия бота при нажатии на кнопку "Vira" - фирма выбранного ранее товара.

            Бот при нажатии на данную кнопку высылает фото данного товара, которое открывается по ссылке из памяти компьютера.
            А потом из базы данных "favorable_prices" и таблицы "Spiral_drills" скидывает пользователю описание, ссылку на этот
            товар (в каком магазине купить его и по какой цене).
            """
            chat_id = message.chat.id
            with open('images/Сверла спиральные vira.webp', 'rb') as file:
                photo = file.read()
            bot.send_photo(chat_id, photo)
            information_database = spiral_drills(2)
            bot.send_message(chat_id, information_database)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')

        @bot.message_handler(func=lambda message: message.text == 'Heller')
        def heller_company_product_information(message):
            """
            Действия бота при нажатии на кнопку "Heller" - фирма выбранного ранее товара.

            Бот при нажатии на данную кнопку высылает фото данного товара, которое открывается по ссылке из памяти компьютера.
            А потом из базы данных "favorable_prices" и таблицы "Spiral_drills" скидывает пользователю описание, ссылку на этот
            товар (в каком магазине купить его и по какой цене).
            """

            chat_id = message.chat.id
            with open('images/Свёрла Heller.webp', 'rb') as file:
                photo = file.read()
            bot.send_photo(chat_id, photo)
            information_database = spiral_drills(3)
            bot.send_message(chat_id, information_database)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')


@bot.message_handler(func=lambda message: message.text == 'Диски для болгарки')
def buttons_of_special_discs_for_grinder(message):
    """
    Действия бота при нажатии на кнопку "Диски для болгарки" пользователем.

    При нажатии на кнопку "Диски для болгарки", пользователю выдаётся 2 новых кнопки на клавиатуре:
    "Резка", "Шлифовка" - это кнопки, с помощью которых можно выбрать тип диска
    (его предназначение, например для резки металла или его шлифовки).
    """
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_price = telebot.types.KeyboardButton(text='Резка')
    button_price2 = telebot.types.KeyboardButton(text='Шлифовка')
    button_price3 = telebot.types.KeyboardButton(text='Выход на главное меню')
    keyboard.add(button_price, button_price2, button_price3)
    bot.send_message(chat_id, 'Выберите тип диска (для какого вида использования): ', reply_markup=keyboard)

    @bot.message_handler(func=lambda message: message.text == 'Резка')
    def buttons_of_cutting_of_firm_of_discs_for_grinder(message):
        """
        Действия бота при нажатии на кнопку "Резка" - тип диска (для каких работ предназначается).

        При нажатии на кнопку "Резка", пользователю выдаётся 2 новых кнопки на клавиатуре:
        "LUGAABRASIV", "ЗУБР" - это фирмы производителей выбранного ранее вида товаров.
        """
        chat_id = message.chat.id
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_price = telebot.types.KeyboardButton(text='LUGAABRASIV')
        button_price2 = telebot.types.KeyboardButton(text='ЗУБР')
        button_price3 = telebot.types.KeyboardButton(text='Выход на главное меню')
        keyboard.add(button_price, button_price2, button_price3)
        bot.send_message(chat_id, 'Выберите фирму: ', reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text == 'LUGAABRASIV')
        def lugaabrasiv_company_product_information(message):
            """
            Действия бота при нажатии на кнопку "LUGAABRASIV" - фирма выбранного ранее товара.

            Бот при нажатии на данную кнопку высылает фото данного товара, которое открывается по ссылке из памяти компьютера.
            А потом из базы данных "favorable_prices" и таблицы "Spiral_drills" скидывает пользователю описание, ссылку на этот
            товар (в каком магазине купить его и по какой цене).
            """
            chat_id = message.chat.id
            with open('images/Диск для болгарки по металлу 125x1.2.png', 'rb') as file:
                photo = file.read()
            bot.send_photo(chat_id, photo)
            information_database = discs_for_grinder(1)
            bot.send_message(chat_id, information_database)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')

        @bot.message_handler(func=lambda message: message.text == 'ЗУБР')
        def zubr_company_product_information(message):
            """
            Действия бота при нажатии на кнопку "ЗУБР" - фирма выбранного ранее товара.

            Бот при нажатии на данную кнопку высылает фото данного товара, которое открывается по ссылке из памяти компьютера.
            А потом из базы данных "favorable_prices" и таблицы "Discs_for_grinder" скидывает пользователю описание, ссылку на этот
            товар (в каком магазине купить его и по какой цене).
            """

            chat_id = message.chat.id
            with open('images/Диск по металлу болгарка зубр.webp', 'rb') as file:
                photo = file.read()
            bot.send_photo(chat_id, photo)
            information_database = discs_for_grinder(2)
            bot.send_message(chat_id, information_database)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')

    @bot.message_handler(func=lambda message: message.text == 'Шлифовка')
    def buttons_of_grinding_of_firm_of_discs_for_grinder(message):
        """
        Действия бота при нажатии на кнопку "Шлифовка" - тип диска (для каких работ предназначается).

        При нажатии на кнопку "Шлифовка", пользователю выдаётся 2 новых кнопки на клавиатуре:
        "Rexant", "Vira" - это фирмы производителей выбранного ранее вида товаров.
        """
        chat_id = message.chat.id
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_price = telebot.types.KeyboardButton(text='Rexant')
        button_price2 = telebot.types.KeyboardButton(text='Vira')
        button_price3 = telebot.types.KeyboardButton(text='Выход на главное меню')
        keyboard.add(button_price, button_price2, button_price3)
        bot.send_message(chat_id, 'Выберите фирму: ', reply_markup=keyboard)

        @bot.message_handler(func=lambda message: message.text == 'Rexant')
        def rexant_company_product_information(message):
            """
            Действия бота при нажатии на кнопку "Rexant" - фирма выбранного ранее товара.

            Бот при нажатии на данную кнопку высылает фото данного товара, которое открывается по ссылке из памяти компьютера.
            А потом из базы данных "favorable_prices" и таблицы "Discs_for_grinder" скидывает пользователю описание, ссылку на этот
            товар (в каком магазине купить его и по какой цене).
            """
            chat_id = message.chat.id
            with open('images/Лепестковый диск rexant + 1 фото.webp', 'rb') as file:
                photo = file.read()
                bot.send_photo(chat_id, photo)
            with open('images/+ 1 фото Rexant.webp', 'rb') as file:
                photo = file.read()
                bot.send_photo(chat_id, photo)
            information_database = discs_for_grinder(3)
            bot.send_message(chat_id, information_database)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')

        @bot.message_handler(func=lambda message: message.text == 'Vira')
        def vira_company_product_information_for_grinder(message):
            """
            Действия бота при нажатии на кнопку "Vira" - фирма выбранного ранее товара.

            Бот при нажатии на данную кнопку высылает фото данного товара, которое открывается по ссылке из памяти компьютера.
            А потом из базы данных "favorable_prices" и таблицы "discs_for_grinder" скидывает пользователю описание, ссылку на этот
            товар (в каком магазине купить его и по какой цене).
            """
            chat_id = message.chat.id
            with open('images/1 фото Vira лепестковый диск.jpg', 'rb') as file:
                photo = file.read()
                bot.send_photo(chat_id, photo)
            with open('images/Диск лепестковый Vira + 1 фото.jpg', 'rb') as file:
                photo = file.read()
                bot.send_photo(chat_id, photo)
            information_database = discs_for_grinder(4)
            bot.send_message(chat_id, information_database)
            bot.send_message(chat_id, 'Вот вся информация о данном товаре')


"""
Осуществляет запуск бота.
"""

if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
