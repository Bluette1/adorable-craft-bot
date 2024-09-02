import re
import requests

BOT_TOKEN = "7244690088:AAGmqESO_5VrxTg7BbfNkInzG5uIMW5ajB4"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/"


def handle_update(update):
    message = update.get("message", {})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "")

    if text == "/start":
        send_message(chat_id, "Welcome to the bot!")

    else:
        text = re.sub(r"\W", "_", text)
        url = "https://robohash.org/{}.png".format(text.strip())
        send_photo(chat_id, url)


def send_message(chat_id, text):
    url = TELEGRAM_API_URL + "sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)


def send_photo(chat_id, photo_url):
    url = TELEGRAM_API_URL + "sendPhoto"
    payload = {"chat_id": chat_id, "photo": photo_url}
    response = requests.post(url, json=payload)

    if response.status_code == 200:
      print("Photo sent successfully!")
    else:
      print("Failed to send photo: please try using different text", response.text)
