# botserver.py — минимальный каркас Flask-приложения
#
# ⚠️ Здесь будет вся логика Telegram-бота.
#    Пока оставляем заглушку, чтобы PythonAnywhere смог запустить сервер.

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def webhook():
    # TODO: сюда позже вставим обработку Telegram-вебхука
    return 'OK', 200

