import telebot
import requests
import os
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CANALI = os.getenv("CANALI").split(",")
DISCLAIMER = os.getenv("DISCLAIMER")
FREQUENZA_MINUTI = int(os.getenv("FREQUENZA_MINUTI"))
GLITCH_TAG = os.getenv("GLITCH_TAG")
NOME_BOT = os.getenv("NOME_BOT")
SVAPO_TRACKING = os.getenv("SVAPO_TRACKING")
SVAPO_URL_BASE = os.getenv("SVAPO_URL_BASE")

bot = telebot.TeleBot(BOT_TOKEN)

def get_offerte():
    return [
        {
            "titolo": "Lampada LED -70%",
            "link": f"https://www.amazon.it/dp/B0772P6LJW?tag={os.getenv('AFFILIATE_ID')}",
            "immagine": "https://m.media-amazon.com/images/I/61b+W1xWRTL._AC_SL1000_.jpg"
        },
        {
            "titolo": "🔥 Offerta SvapoStore: Aroma premium a 2,99€!",
            "link": f"{SVAPO_URL_BASE}?tracking={SVAPO_TRACKING}",
            "immagine": "https://www.svapostore.net/media/catalog/product/cache/926507dc7f93631a094422215b778fe0/image/750x750/9df78eab33525d08d6e5fb8d27136e95/a/r/aroma_3_1.jpg"
        }
    ]

def pubblica_offerta(canale, offerta):
    try:
        messaggio = f"{offerta['titolo']}
{DISCLAIMER}
{offerta['link']}"
        bot.send_photo(chat_id=canale.strip(), photo=offerta['immagine'], caption=messaggio)
        print(f"Inviato su {canale}")
    except Exception as e:
        print(f"Errore su {canale}: {e}")

while True:
    offerte = get_offerte()
    for canale in CANALI:
        for offerta in offerte:
            pubblica_offerta(canale, offerta)
    print("Atteso prossima pubblicazione...")
    time.sleep(FREQUENZA_MINUTI * 60)
