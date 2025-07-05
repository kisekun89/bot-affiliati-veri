import os
import time
import telebot
import random

bot_token = os.getenv("BOT_TOKEN")
chat_ids = os.getenv("CANALI", "").split(",")

bot = telebot.TeleBot(bot_token)

# OFFERTE FORMATTATE CORRETTAMENTE
offerte = [
    "🔥 [Amazon] Lampada LED -70% → https://www.amazon.it/dp/B0772P6LJW/?tag=affaritech21-21",
    "🔥 [Amazon] Powerbank 10000mAh -40% → https://www.amazon.it/dp/B09N4XQG5B/?tag=affaritech21-21",
    "🔥 [SvapoStore] Aroma premium a 2,99€! → https://www.svapostore.net/?tracking=jD7Vnx8Leh2ABPYfEX9LoaSYXtDy6ePBMdWX6kaN5bViiEaB4450Wx2NuOUceDNF",
    "🔥 [SvapoStore] Kit ELFX Pro scontato → https://www.svapostore.net/kit-sigarette-elettroniche/elfbar-elfx-pro-pod-kit?tracking=jD7Vnx8Leh2ABPYfEX9LoaSYXtDy6ePBMdWX6kaN5bViiEaB4450Wx2NuOUceDNF",
    "🔥 [Amazon] Ciabatta multipresa Smart -50% → https://www.amazon.it/dp/B07ZP6FK8L/?tag=affaritech21-21",
]

frequenza_minuti = int(os.getenv("FREQUENZA_MINUTI", 15))

def invia_offerta():
    messaggio = random.choice(offerte)
    for chat_id in chat_ids:
        try:
            bot.send_message(chat_id.strip(), messaggio)
        except Exception as e:
            print(f"Errore invio a {chat_id}: {e}")

while True:
    invia_offerta()
    time.sleep(frequenza_minuti * 15)
