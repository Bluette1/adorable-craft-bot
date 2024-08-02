import requests

BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
WEBHOOK_URL = 'https://yourdomain.com/webhook'  # Replace with your actual URL

url = f'https://api.telegram.org/bot{BOT_TOKEN}/setWebhook'
payload = {'url': WEBHOOK_URL}

response = requests.post(url, json=payload)
print(response.json())
