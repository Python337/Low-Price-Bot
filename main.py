import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

users = {}


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id,
                     'Добро пожаловать в бота сбора обратной связи! Введите свой логин: ')
    users[chat_id] = {}
    bot.register_next_step_handler(message, save_username)


def save_username(message):
    chat_id = message.chat.id
    login = message.text
    users[chat_id] = login
    bot.send_message(chat_id,
                     f'Отлично, {login}. Теперь укажи свою пароль для входа в систему')


if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()