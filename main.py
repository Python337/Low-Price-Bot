import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

users = {}


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_price = telebot.types.KeyboardButton(text='Выход')
    button_price2 = telebot.types.KeyboardButton(text='Поиск товара')
    keyboard.add(button_price, button_price2)
    bot.send_message(chat_id,
                     'Добро пожаловать в бота для поиска товаров на складе. Этот бот напишет, где хранится интересующий товар.',
                     reply_markup=keyboard)

@bot.message_handler(
    func=lambda message: message.text == 'Поиск товара')
def write_to_support(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Введите название товара: ')
    users[chat_id] = {}
    bot.register_next_step_handler(message, save_username)


def save_username(message):
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    bot.send_message(chat_id, f'Отлично. Теперь укажите по ценовому диапозону товар, так как возможно есть несколько разных производителей данного товара:')
    button_price = telebot.types.InlineKeyboardButton(text="Дешёво")

    button_price2 = telebot.types.InlineKeyboardButton(text="Средняя")

    button_price3 = telebot.types.InlineKeyboardButton(text="Дорого")

    keyboard.add(button_price, button_price2, button_price3)


def save_surname(message):
    chat_id = message.chat.id
    surname = message.text
    users[chat_id]['surname'] = surname
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_save = telebot.types.InlineKeyboardButton(text="Сохранить")
    button_change = telebot.types.InlineKeyboardButton(text="Изменить")

    keyboard.add(button_save, button_change)

    bot.send_message(chat_id, f'Сохранить данные?', reply_markup=keyboard)


@bot.message_handler(commands=['who_i'])
def who_i(message):
    chat_id = message.chat.id
    name = users[chat_id]['name']
    surname = users[chat_id]['surname']
    bot.send_message(chat_id, f'Вы: {name} {surname}')


@bot.callback_query_handler(func=lambda call: call.data == 'save_data')
def save_btn(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                         text='Данные сохранены!')


@bot.callback_query_handler(func=lambda call: call.data == 'change_data')
def save_btn(call):
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                         text='Изменение данных!')
    write_to_support(message)


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()