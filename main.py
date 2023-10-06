import telebot
import requests
import json
from baseinfo import weathermap_token, bot_token




bot = telebot.TeleBot(bot_token)






@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добрый день! Введите название города")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weathermap_token}&units=metric')
    if weather.status_code == 200:
        data = json.loads(weather.text)
        bot.reply_to(message, f'На данный момент: {data["main"]["temp"]}')
    else:
        bot.reply_to(message, f'Неверное название города')





bot.polling(none_stop=True)


