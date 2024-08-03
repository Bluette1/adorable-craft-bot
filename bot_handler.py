import requests

BOT_TOKEN = '7244690088:AAGmqESO_5VrxTg7BbfNkInzG5uIMW5ajB4'
TELEGRAM_API_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

def handle_update(update):
    message = update.get('message', {})
    chat_id = message.get('chat', {}).get('id')
    text = message.get('text', '')

    if text == '/start':
        send_message(chat_id, 'Welcome to the bot!')

def send_message(chat_id, text):
    url = TELEGRAM_API_URL + 'sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    requests.post(url, json=payload)
