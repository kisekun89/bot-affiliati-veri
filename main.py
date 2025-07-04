import os
import time
import random
import telebot

bot_token = os.getenv("BOT_TOKEN")
chat_ids = os.getenv("CANALI").split(",")
frequenza_minuti = int(os.getenv("FREQUENZA_MINUTI"))
affiliate_id = os.getenv("AFFILIATE_ID")
svapo_tracking = os.getenv("SVAPO_TRACKING")

bot = telebot.TeleBot(bot_token)

offerte = [
    f"🔥 [Amazon] Lampada LED -70% ➜ https://www.amazon.it/dp/B07ZP6LJWG?tag={affiliate_id}",
    f"💨 [SvapoStore] ELFX Pro in sconto ➜ https://www.svapostore.net/kit-sigarette-elettroniche/elfbar-elfx-pro-pod-kit?tracking={svapo_tracking}",
    f"🧪 [SvapoStore] Glicerina 500ml ➜ https://www.svapostore.net/liquidi-fai-da-te/vapefactory-glicerina-vegetale-500ml?tracking={svapo_tracking}"
]

def invia_offerta():
    messaggio = random.choice(offerte)
    for chat_id in chat_ids:
        try:
            bot.send_message(chat_id.strip(), messaggio)
        except Exception as e:
            print(f"Errore nell'invio a {chat_id}: {e}")

# Loop infinito
while True:
    invia_offerta()
    time.sleep(frequenza_minuti * 15)
