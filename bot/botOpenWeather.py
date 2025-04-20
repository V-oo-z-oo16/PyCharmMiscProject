import telebot
from telebot import types
import requests
import threading
import time
import json

token = '7509346747:AAHE776B6FJbm3u28cx37nBoGDxxBK3HNq4'
api_key = '019c7e7223489dcc9ee589d1f4d188dc'
bot = telebot.TeleBot(token)


users_db = {}


def load_users():
    global users_db
    try:
        with open('users.json', 'r') as f:
            users_db = json.load(f)
    except:
        pass


def save_users():
    with open('users.json', 'w') as f:
        json.dump(users_db, f)


load_users()

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': data['name'],
            'temp': data['main']['temp'],
            'desc': data['weather'][0]['description']
        }
    return None


def weather_monitor():
    while True:
        for chat_id, city in users_db.copy().items():
            current = fetch_weather(city)
            if not current: continue

            msg = f"🌤️ Текущая погода в {current['city']}:\n"
            msg += f"Температура: {current['temp']}°C\n"
            msg += f"Состояние: {current['desc'].capitalize()}"
            bot.send_message(chat_id, msg)

        time.sleep(3600)



@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id, "🌍 Введите ваш город для регистрации:")
    bot.register_next_step_handler(msg, process_city)


def process_city(message):
    city = message.text
    weather = fetch_weather(city)
    if weather:
        users_db[str(message.chat.id)] = city
        save_users()
        bot.send_message(message.chat.id, f"✅ Регистрация завершена! Ваш город: {weather['city']}")
        button(message.chat.id)
    else:
        bot.send_message(message.chat.id, "❌ Город не найден. Попробуйте снова /start")

def button(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Мой город")
    btn2 = types.KeyboardButton("Сменить город")
    btn3 = types.KeyboardButton("Погода в другом городе")
    markup.add(btn1, btn2, btn3)
    bot.send_message(chat_id, "Выберите действие:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Погода в другом городе")
def ask_other_city(message):
    msg = bot.send_message(message.chat.id, "🌍 Введите название города, чтобы узнать погоду:")
    bot.register_next_step_handler(msg, show_other_city_weather)

def show_other_city_weather(message):
    city = message.text
    weather = fetch_weather(city)
    if weather:
        bot.reply_to(message, f"🌤️ Погода в городе {weather['city']}:\nТемпература: {weather['temp']}°C\nСостояние: {weather['desc']}")
    else:
        bot.reply_to(message, "❌ Город не найден. Попробуйте ввести название еще раз.")
        msg = bot.send_message(message.chat.id, "Введите название города еще раз:")
        bot.register_next_step_handler(msg, show_other_city_weather)


@bot.message_handler(func=lambda m: m.text == "Мой город")
def show_weather(message):
    if str(message.chat.id) in users_db:
        city = users_db[str(message.chat.id)]
        weather = fetch_weather(city)
        bot.reply_to(message, f"🌤️ В {weather['city']} сейчас {weather['temp']}°C, {weather['desc']}")
    else:
        bot.send_message(message.chat.id, "❌ Вы не зарегистрированы. Введите /start")


@bot.message_handler(func=lambda m: m.text == "Сменить город")
def change_city(message):
    msg = bot.send_message(message.chat.id, "🌍 Введите новый город:")
    bot.register_next_step_handler(msg, process_city)


threading.Thread(target=weather_monitor, daemon=True).start()
bot.polling(none_stop=True)
