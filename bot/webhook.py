import requests

from .credentials import BOT_TOKEN

WEBHOOK_URL = 'https://adorable-avatar-craft-bot-cd62f4a07dce.herokuapp.com/webhook'  # Replace with your actual URL

url = f'https://api.telegram.org/bot{BOT_TOKEN}/setWebhook'
payload = {'url': WEBHOOK_URL}

response = requests.post(url, json=payload)
print(response.json())
