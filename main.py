import os
import time
import telebot  # da pyTelegramBotAPI
import random

bot_token = os.getenv("BOT_TOKEN")
chat_ids = os.getenv("CHAT_IDS").split(",")

bot = telebot.TeleBot(bot_token)

# Offerte vere statiche (esempio), includendo Amazon + SvapoStore
offerte = [
    "🔥 [Amazon] Lampada LED scontata del 70%! ➡️ https://amzn.to/3XEXAMPLE",
    "💨 [SvapoStore] Elfbar ELFX Pro Pod Kit scontato! ➡️ https://www.svapostore.net/kit-sigarette-elettroniche/elfbar-elfx-pro-pod-kit?tracking=jD7Vnx8Leh2ABPYfEX9LOaSYXtDy6ePBMdWX6kaN5bViiEaB4450Wx2NuOUceDNF",
    "🧴 [SvapoStore] Glicerina vegetale 500ml ➡️ https://www.svapostore.net/liquidi-fai-da-te/vapefactory-glicerina-vegetale-500ml?tracking=jD7Vnx8Leh2ABPYfEX9LOaSYXtDy6ePBMdWX6kaN5bViiEaB4450Wx2NuOUceDNF"
]

while True:
    offerta = random.choice(offerte)
    for chat_id in chat_ids:
        try:
            bot.send_message(chat_id.strip(), offerta)
        except Exception as e:
            print(f"Errore inviando a {chat_id}: {e}")
    time.sleep(900)  # 15 minuti
