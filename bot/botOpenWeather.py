import telebot
import requests
token = '7509346747:AAHE776B6FJbm3u28cx37nBoGDxxBK3HNq4'
api_key = '019c7e7223489dcc9ee589d1f4d188dc'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def main(message):
    bot.reply_to(message, "Используйте команду /weather <город>, чтобы получить погоду")

@bot.message_handler(commands=['weather'])
def get_weather(message):
    city_parts = message.text.split()
    if len(city_parts) > 1:
        city = ' '.join(city_parts[1:])
    else:
        city = None


    if city:
        weather_info = fetch_weather(city)
        bot.reply_to(message, weather_info)
    else:
        bot.reply_to(message, "укажите город пример: /weather Москва")


def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        return f"Погода в {city_name}: {temperature}°C, {weather_description}"
    else:
        return "Город не найден. Пожалуйста, проверьте название"

bot.polling(none_stop=True)