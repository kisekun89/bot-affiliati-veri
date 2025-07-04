import telebot
import os
import time
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CANALI = os.getenv("CANALI", "").split(",")
FREQUENZA_MINUTI = int(os.getenv("FREQUENZA_MINUTI", "60"))

AMAZON_ID = "affaritech21-21"
SVAPO_TRACKING = "jD7Vnx8Leh2ABPYfEX9LOaSYXtDy6ePBMdWX6kaN5bViiEaB4450Wx2NuOUceDNF"

bot = telebot.TeleBot(BOT_TOKEN)

def get_offerta_reale(canale):
    if "svapo" in canale:
        return f"🔥 Offerta SvapoStore:\n👉 Aroma premium in sconto!\n🔗 https://www.svapostore.net/?tracking={SVAPO_TRACKING}"
    else:
        # OFFERTA AMAZON REALE CON LINK FUNZIONANTE
        asin = "B08XMBLKR2"  # esempio reale funzionante
        return f"🔥 Powerbank 20000mAh in sconto!\n✅ Spedito da Amazon\n🔗 https://www.amazon.it/dp/{asin}?tag={AMAZON_ID}"

def pubblica_offerte():
    for canale in CANALI:
        try:
            testo = get_offerta_reale(canale)
            bot.send_message(canale.strip(), testo)
            print(f"✅ Inviato su {canale}")
        except Exception as e:
            print(f"❌ Errore su {canale}: {e}")

while True:
    pubblica_offerte()
    time.sleep(FREQUENZA_MINUTI * 60)
