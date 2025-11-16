from telethon import TelegramClient, events
import os
import requests

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
webhook_url = os.environ.get("N8N_WEBHOOK")

client = TelegramClient("anon", api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    message = event.raw_text
    payload = {
        "username": sender.username if sender.username else "unknown",
        "message": message,
    }
    try:
        requests.post(webhook_url, json=payload)
    except Exception as e:
        print(f"Erro ao enviar para n8n: {e}")

print("Userbot iniciado! Aguardando mensagens...")
client.start()
client.run_until_disconnected()
