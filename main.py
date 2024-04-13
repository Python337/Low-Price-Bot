import telebot
from config import TOKEN
from bd import get

bot = telebot.TeleBot(TOKEN)

slov = {}
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
    button_price = telebot.types.KeyboardButton(text='Гвозди 120x4 мм')
    button_price2 = telebot.types.KeyboardButton(text='Сверло перовое')
    button_price3 = telebot.types.KeyboardButton(text='Сверло спиральное')
    button_price4 = telebot.types.KeyboardButton(text='Саморезы 3.5x25 мм')
    button_price5 = telebot.types.KeyboardButton(text='Выход на главное меню')
    keyboard.add(button_price, button_price2, button_price3, button_price4, button_price5)
    bot.send_message(chat_id, 'Выберите товар из предложенного списка: ', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Сверло перовое')
def button(message):
    chat_id = message.chat.id
    slov[chat_id] = message.text
    with open('images/Сверло перовое 20 мм.jpg', 'rb') as file:
        photo = file.read()
    bot.send_photo(chat_id, photo)
    a = get(1)
    bot.send_message(chat_id, a)



@bot.message_handler(func=lambda message: message.text == 'Сверло спиральное')
def button(message):
    chat_id = message.chat.id
    with open('images/Сверло спиральное 90 мм.webp', 'rb') as file:
        photo = file.read()
    bot.send_photo(chat_id, photo)
    a = get(2)
    bot.send_message(chat_id, a)


@bot.message_handler(func=lambda message: message.text == 'Саморезы 3.5x25 мм')
def button(message):
    chat_id = message.chat.id
    with open('images/Саморезы 3.5x25 мм.webp', 'rb') as file:
        photo = file.read()
    bot.send_photo(chat_id, photo)
    a = get(3)
    bot.send_message(chat_id, a)


@bot.message_handler(func=lambda message: message.text == 'Гвозди 120x4 мм')
def button(message):
    chat_id = message.chat.id
    with open('images/Гвозди строительные 120x4 мм.jpg', 'rb') as file:
        photo = file.read()
    bot.send_photo(chat_id, photo)
    a = get(4)
    bot.send_message(chat_id, a)


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()


