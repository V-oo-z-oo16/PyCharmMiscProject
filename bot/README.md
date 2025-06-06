botOpenWeather.py
Этот скрипт реализует Telegram-бота для получения прогноза погоды с помощью OpenWeather API.

Возможности
Получение текущей погоды по названию города.

Удобный интерфейс через Telegram-бота.

Поддержка различных погодных параметров (температура, влажность, ветер и др.).

Требования
Python 3.7+

Библиотеки:

python-telegram-bot

requests

Установка
Клонируйте репозиторий:

bash
git clone https://github.com/V-oo-z-oo16/PyCharmMiscProject.git
cd PyCharmMiscProject/bot
Установите зависимости:

bash
pip install -r requirements.txt
Если файла requirements.txt нет, установите вручную:

bash
pip install python-telegram-bot requests
Получите API-ключи:

Telegram Bot Token

OpenWeather API Key

Укажите ваши ключи в коде или в переменных окружения.

Использование
Запустите бота командой:

bash
python botOpenWeather.py
Далее найдите бота в Telegram и начните диалог. Введите название города, чтобы получить прогноз погоды.

Пример работы
text
Вы: Москва
Бот: Погода в Москве: +18°C, облачно, ветер 3 м/с.
Настройки
Вы можете изменить язык, формат вывода и другие параметры в коде файла botOpenWeather.py.

Лицензия
MIT License