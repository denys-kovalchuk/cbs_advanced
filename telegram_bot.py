import telebot
from settings import TELEGRAM_BOT_TOKEN
from weather import weather, get_image


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    button = telebot.types.InlineKeyboardButton('Start', callback_data='start')

    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(button)
    bot.send_message(message.chat.id, f"Hello, {message.from_user.first_name}!\n"
                                      f"Welcome to weather bot\n"
                                      f"Choose an option: ", reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton('Message the developer', url='t.me/us3nam33'))
    bot.send_message(message.chat.id,
                     '1) To get weather in a city press /start\n' +
                     '2) Type a city\n' +
                     '3) You will receive a message containing weather info in the selected city',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    bot.answer_callback_query(call.id)
    request_city(call.message)


def request_city(message):
    bot.send_message(message.chat.id, 'Please type a city: ')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if not weather(message.text):
        wrong_city(message)
    else:
        bot.send_photo(message.chat.id, get_image(weather(message.text)[1], weather(message.text)[2]))
        bot.send_message(message.chat.id, weather(message.text)[0])
        request_city(message)


def wrong_city(message):
    bot.send_message(message.chat.id, 'Wrong input, there is no such city, try again')


bot.infinity_polling()
