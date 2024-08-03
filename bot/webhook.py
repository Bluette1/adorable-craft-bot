import requests

BOT_TOKEN = '7244690088:AAGmqESO_5VrxTg7BbfNkInzG5uIMW5ajB4'
WEBHOOK_URL = 'https://adorable-craft-bot-7a8e1764f1a3.herokuapp.com/webhook'  # Replace with your actual URL

url = f'https://api.telegram.org/bot{BOT_TOKEN}/setWebhook'
payload = {'url': WEBHOOK_URL}

response = requests.post(url, json=payload)
print(response.json())
