from flask import Flask, request
from .bot_handler import handle_update


def init_app(app: Flask):
    @app.route("/webhook", methods=["POST"])
    def webhook():
        if request.method == "POST":
            update = request.get_json()
            handle_update(update)
            return "OK"
