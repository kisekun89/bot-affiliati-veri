import os
import telebot
import time
import requests
import random

BOT_TOKEN = os.environ['BOT_TOKEN']
CANALI = os.environ['CANALI'].split(',')
DISCLAIMER = os.environ['DISCLAIMER']
FREQUENZA_MINUTI = int(os.environ['FREQUENZA_MINUTI'])
GLITCH_TAG = os.environ['GLITCH_TAG']
NOME_BOT = os.environ['NOME_BOT']
AFFILIATE_ID = os.environ['AFFILIATE_ID']
SVAPO_TRACKING = os.environ['SVAPO_TRACKING']
SVAPO_URL_BASE = os.environ['SVAPO_URL_BASE']

bot = telebot.TeleBot(BOT_TOKEN)

def get_offerta_amazon():
    prodotti = [
        {
            "titolo": "🔥 [Amazon] Lampada LED -70%",
            "link": f"https://www.amazon.it/dp/B0772P6LJW?tag={AFFILIATE_ID}",
            "immagine": "https://m.media-amazon.com/images/I/71V--WPtKYL._AC_SL1500_.jpg"
        },
        {
            "titolo": "🎧 [Amazon] Cuffie Bluetooth in offerta",
            "link": f"https://www.amazon.it/dp/B09NQ1L1RS?tag={AFFILIATE_ID}",
            "immagine": "https://m.media-amazon.com/images/I/61Nw5ZWhKYL._AC_SL1500_.jpg"
        }
    ]
    return random.choice(prodotti)

def get_offerta_svapo():
    return {
        "titolo": "🔥 Offerta SvapoStore: Aroma premium a 2,99€!",
        "link": f"{SVAPO_URL_BASE}?tracking={SVAPO_TRACKING}"
    }

def invia_offerta(canale, offerta, immagine=None):
    testo = f"{offerta['titolo']}\n{offerta['link']}\n\n{DISCLAIMER}"
    try:
        if immagine:
            bot.send_photo(canale.strip(), immagine, caption=testo, disable_web_page_preview=True)
        else:
            bot.send_message(canale.strip(), testo, disable_web_page_preview=True)
        print(f"✅ Inviato su {canale.strip()}")
    except Exception as e:
        print(f"❌ Errore su {canale.strip()}: {e}")

while True:
    for canale in CANALI:
        if "svapo" in canale:
            offerta = get_offerta_svapo()
            invia_offerta(canale, offerta)
        else:
            offerta = get_offerta_amazon()
            invia_offerta(canale, offerta, immagine=offerta["immagine"])
    print("⏳ Attesa prossima pubblicazione...")
    time.sleep(FREQUENZA_MINUTI * 15)
