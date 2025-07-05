import os
import time
import requests
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CANALI = os.getenv("CANALI", "").split(",")
FREQUENZA_MINUTI = int(os.getenv("FREQUENZA_MINUTI", "15"))
SVAPO_TRACKING = os.getenv("SVAPO_TRACKING", "")
AMAZON_TAG = os.getenv("AMAZON_TAG", "affaritech21-21")

bot = telebot.TeleBot(BOT_TOKEN)

# 🔧 Esempi temporanei (da sostituire con database offerte vere)
OFFERTE = [
    {
        "titolo": "Powerbank 20000mAh",
        "prezzo": "14,99€",
        "immagine": "https://m.media-amazon.com/images/I/61B04f0ALWL._AC_SL1500_.jpg",
        "link": f"https://www.amazon.it/dp/B08XMBLKR2/?tag={AMAZON_TAG}",
        "tipo": "amazon"
    },
    {
        "titolo": "Aroma Madagascar 10ml",
        "prezzo": "2,99€",
        "immagine": "https://www.svapostore.net/media/catalog/product/cache/1/image/600x/040ec09b1e35df139433887a97daa66f/m/a/madagascar.jpg",
        "link": f"https://www.svapostore.net/liquidi-fai-da-te/super-flavor-aroma-madagascar-10ml?tracking={SVAPO_TRACKING}",
        "tipo": "svapo"
    }
]

def filtra_offerta(canale, offerta):
    if "svapo" in canale and offerta["tipo"] == "svapo":
        return True
    elif "svapo" not in canale and offerta["tipo"] == "amazon":
        return True
    return False

def pubblica_offerte():
    for canale in CANALI:
        for offerta in OFFERTE:
            if filtra_offerta(canale, offerta):
                try:
                    testo = f"🔥 {offerta['titolo']}\n💰 {offerta['prezzo']}\n🔗 {offerta['link']}"
                    bot.send_photo(canale.strip(), photo=offerta["immagine"], caption=testo)
                    print(f"✅ Inviato su {canale}")
                    break  # Una sola offerta per canale ogni 15 minuti
                except Exception as e:
                    print(f"❌ Errore su {canale}: {e}")

while True:
    pubblica_offerte()
    time.sleep(FREQUENZA_MINUTI * 15)
