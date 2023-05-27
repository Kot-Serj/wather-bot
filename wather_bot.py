import telebot
from api import bot
from get_data import get_temp_and_date
from log import log


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выбери город")

    # Обрабатываем входящие текстовые сообщения
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city_name = message.text.strip().lower() #переменная для функции
    if get_temp_and_date(city_name):
        weather_message = (
            f"Текущая температура в городе {city_name.title()}: {(get_temp_and_date(city_name))['temperature']}\n" 
            f"Влажность: {(get_temp_and_date(city_name))['humidity']}\n" 
            f"Давление: {(get_temp_and_date(city_name))['pressure']} \n" 
            f"Скорость ветра: {(get_temp_and_date(city_name))['wind_speed']}\n" 
            f"Дата и время: {(get_temp_and_date(city_name))['date']}"
        )
    else:
        weather_message = f"Извините, не удалось получить данные о погоде в городе {city_name.title()}. Пожалуйста, проверьте правильность названия города и попробуйте еще раз."
    bot.send_message(message.chat.id, weather_message)
    log(message)

bot.polling(none_stop=True)