import os
import requests
import random
import telebot
import time

# --- CONFIG ---
BOT_TOKEN = os.getenv("BOT_TOKEN")
CANALI = os.getenv("CANALI").split(",")
AFFILIATE_ID = os.getenv("AFFILIATE_ID")
DISCLAIMER = os.getenv("DISCLAIMER", "")
FREQUENZA_MINUTI = int(os.getenv("FREQUENZA_MINUTI", 60))
GLITCH_TAG = os.getenv("GLITCH_TAG", "")
SVAPO_TRACKING = os.getenv("SVAPO_TRACKING", "")
SVAPO_URL_BASE = os.getenv("SVAPO_URL_BASE", "https://www.svapostore.net")

bot = telebot.TeleBot(BOT_TOKEN)

# --- FUNZIONI DI RACCOLTA OFFERTE ---

def ottieni_offerte_amazon():
    # Placeholder: Simulazione con offerte statiche (da sostituire con scraping o API reali)
    offerte = [
        {
            "titolo": "[Amazon] Cuffie Bluetooth – 75%",
            "prezzo": "19,99€",
            "link": f"https://www.amazon.it/dp/B08P2CL6Y2?tag={AFFILIATE_ID}",
            "immagine": "https://m.media-amazon.com/images/I/61oYYFq1+wL._AC_SL1500_.jpg"
        },
        {
            "titolo": "[Amazon] Lampada LED Intelligente – 60%",
            "prezzo": "14,90€",
            "link": f"https://www.amazon.it/dp/B07P6LJWGT?tag={AFFILIATE_ID}",
            "immagine": "https://m.media-amazon.com/images/I/71P0v3mAq7L._AC_SL1500_.jpg"
        }
    ]
    return offerte

def ottieni_offerte_svapo():
    return [
        {
            "titolo": "🔥 Aroma Premium Svapo a 2,99€!",
            "prezzo": "2,99€",
            "link": f"{SVAPO_URL_BASE}/liquidi-fai-da-te/super-flavor-aroma-madagascar-10ml?tracking={SVAPO_TRACKING}",
            "immagine": "https://www.svapostore.net/media/catalog/product/cache/b4c25b24ad84c7cd21a2eb859994b9e7/s/u/super_flavor_aroma_madagascar.jpg"
        }
    ]

# --- FUNZIONE DI PUBBLICAZIONE ---

def pubblica_offerta(canale, offerta):
    messaggio = f"🛒 {offerta['titolo']}\n💰 {offerta['prezzo']}\n🔗 {offerta['link']}\n\n{DISCLAIMER}"
    try:
        if "svapo" in canale:
            bot.send_message(canale.strip(), messaggio)
        else:
            bot.send_photo(canale.strip(), offerta['immagine'], caption=messaggio)
        print(f"✅ Inviato su {canale.strip()}")
    except Exception as e:
        print(f"❌ Errore su {canale.strip()}: {e}")

# --- CICLO PRINCIPALE ---

def ciclo_pubblicazione():
    while True:
        offerte_amazon = ottieni_offerte_amazon()
        offerte_svapo = ottieni_offerte_svapo()

        for canale in CANALI:
            if "svapo" in canale:
                offerta = random.choice(offerte_svapo)
            else:
                offerta = random.choice(offerte_amazon)

            pubblica_offerta(canale, offerta)

        print(f"🕒 Atteso prossima pubblicazione...")
        time.sleep(FREQUENZA_MINUTI * 60)

# --- AVVIO ---

if __name__ == "__main__":
    ciclo_pubblicazione()
