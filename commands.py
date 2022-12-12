from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def weather():
    markup = ReplyKeyboardMarkup(row_width=True, resize_keyboard=True)
    btn = KeyboardButton(text='Погода ☁')
    markup.add(btn)
    return markup