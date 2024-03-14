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
                     'Добро пожаловать в бота для поиска товаров на складе. Этот бот напишет, где хранится интересующий товар.',
                     reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Выход на главное меню')
def back_to_menu(message):
    welcome(message)


button_save = telebot.types.InlineKeyboardButton(text="Сохранить",
                                                 callback_data='save_data')


@bot.message_handler(
    func=lambda message: message.text == 'Поиск товара')
def write_to_support(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Введите название товара: ')
    bot.register_next_step_handler(message, buttons_price)


def buttons_price(message):
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_price = telebot.types.InlineKeyboardButton(text="Дешёво",
                                                      callback_data='cheaply')

    button_price2 = telebot.types.InlineKeyboardButton(text="Средняя",
                                                       callback_data='average')

    button_price3 = telebot.types.InlineKeyboardButton(text="Дорого",
                                                       callback_data='expensive')

    keyboard.add(button_price, button_price2, button_price3)
    bot.send_message(chat_id,
                     f'Отлично. Теперь укажите по ценовому диапозону товар, так как возможно есть несколько разных производителей данного товара:',
                     reply_markup=keyboard)
if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
