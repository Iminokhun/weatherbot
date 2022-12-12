from telebot import TeleBot
from telebot.types import Message
from commands import weather
from weather_api import get_weather

bot = TeleBot('5940200666:AAEewUo1sodfzTuzzeZdY5priEGRbVmxJRg', parse_mode='HTML')

@bot.message_handler(commands=['start'])
def start(message: Message):
    name = message.from_user.username
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Привет <b>{name}</b> хотите узнать погоду", reply_markup=weather())

@bot.message_handler(regexp='Погода ☁')
def start_weather(message: Message):
    bot.send_message(message.chat.id, 'Введите город: ')

@bot.message_handler(content_types=['text'])
def city(message: Message):
    chat_id = message.chat.id
    city = message.text
    answer = get_weather(city)
    bot.send_message(chat_id, answer, reply_markup=weather() )




if __name__ == '__main__':
    bot.polling(none_stop=True)
