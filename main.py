import telebot
import os
import time
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CANALI = os.getenv("CANALI", "").split(",")
FREQUENZA_MINUTI = int(os.getenv("FREQUENZA_MINUTI", "15"))
SVAPO_TRACKING = os.getenv("SVAPO_TRACKING", "")
AMAZON_TAG = os.getenv("AMAZON_TAG", "")

bot = telebot.TeleBot(BOT_TOKEN)

def get_offerta(canale):
    if "svapo" in canale:
        return f"""🔥 Offerta SvapoStore:
👉 Aroma top a prezzo speciale!
🔗 https://www.svapostore.net/?tracking={SVAPO_TRACKING}"""
    else:
        return f"""🔥 Offerta Amazon:
👉 Powerbank 20000mAh solo 14,99€
✅ Spedito da Amazon
🔗 https://www.amazon.it/dp/B08XMBLKR2?tag={AMAZON_TAG}"""

def pubblica_offerte():
    for canale in CANALI:
        try:
            testo = get_offerta(canale.strip())
            bot.send_message(canale.strip(), testo, disable_web_page_preview=True)
            print(f"✅ Pubblicato su {canale}")
        except Exception as e:
            print(f"❌ Errore su {canale}: {e}")

while True:
    pubblica_offerte()
    time.sleep(FREQUENZA_MINUTI * 15)
