from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = requests.get('https://ip-api.com/json').json().get('query', 'Неизвестно')
    country = requests.get('https://ip-api.com/json').json().get('country', 'Неизвестно')
    message = f"Тут был {user_ip} из {country}"
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>GeoLocation</title>
    </head>
    <body>
        <h1>$ERROR</h1>
        <p>{message}</p>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
