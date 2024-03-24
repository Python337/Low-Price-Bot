import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

users = {}


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
    button_price = telebot.types.KeyboardButton(text='Гвозди')
    button_price2 = telebot.types.KeyboardButton(text='Сверло перовое')
    button_price3 = telebot.types.KeyboardButton(text='Сверло спиральное')
    button_price4 = telebot.types.KeyboardButton(text='Саморезы')
    button_price5 = telebot.types.KeyboardButton(text='Гвозди')
    button_price6 = telebot.types.KeyboardButton(text='Выход на главное меню')
    keyboard.add(button_price, button_price2, button_price3, button_price4, button_price5, button_price6)
    bot.send_message(chat_id, 'Выберите товар из предложенного списка: ', reply_markup=keyboard)


# @bot.message_handler(func=lambda message: message.text == 'Гвозди')
# def g():
#     bot.send_message.chat.id(feather_drill())


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()