from telethon import TelegramClient, events
import requests

# === SEUS DADOS DE AUTENTICAÇÃO ===
api_id = 37536236
api_hash = 'b71767892b510a465d47e03dc45405d9'
session_name = 'n8n_session'

# === URL do webhook do n8n ===
n8n_webhook_url = 'https://serven8.automatizacomea.cloud/webhook/telegram-group-listener'

# === INICIALIZA O CLIENTE TELEGRAM ===
client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    try:
        message = event.message.message
        chat = await event.get_chat()
        sender = await event.get_sender()

        payload = {
            'chat_id': chat.id,
            'chat_title': getattr(chat, 'title', 'Private'),
            'sender': sender.username or sender.first_name,
            'message': message
        }

        print(f"[{payload['chat_title']}] {payload['sender']}: {payload['message']}")
        requests.post(n8n_webhook_url, json=payload)

    except Exception as e:
        print(f"[ERRO] {e}")

print("🔁 Conectando ao Telegram...")
client.start()
print("✅ Conectado! Monitorando mensagens...")
client.run_until_disconnected()
