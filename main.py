import time
import requests
from telebot import TeleBot

# Token del bot
TOKEN = '7267062520:AAHPb1Wy1VbsvZ9qBYO-pbaQ6G7PqQbF_KQ'
bot = TeleBot(TOKEN)

# ID canali Telegram
canali = {
    'tech': -1002532953670,
    'casa': -1002768166518,
    'gaming': -1002755987703,
    'offerte': -1002673875319,
    'svapo': -1002523268812
}

# Offerte test funzionanti
def recupera_offerte():
    return [
        {
            'titolo': '⚡ Caricatore USB-C 20W in super offerta!',
            'link': 'https://www.amazon.it/dp/B09XQYZ12Z?tag=affaritech21-21',
            'immagine': 'https://m.media-amazon.com/images/I/61ixPBLqW-L._AC_SL1500_.jpg',
            'categoria': 'tech'
        },
        {
            'titolo': '🔥 Aroma Svapo alla Vaniglia Premium a 2,99€!',
            'link': 'https://www.svapostore.net/liquidi/aroma-vaniglia?tracking=jD7Vnx8Leh2ABPYfEX9LOaSYXtDy6ePBMdWX6kaN5bViiEaB4450Wx2NuOUceDNF',
            'immagine': 'https://www.svapostore.net/media/catalog/product/cache/4/image/800x800/9df78eab33525d08d6e5fb8d27136e95/a/r/aroma-vaniglia.jpg',
            'categoria': 'svapo'
        }
    ]

# Funzione invio automatico
def invia_offerte():
    offerte = recupera_offerte()
    for offerta in offerte:
        messaggio = f"{offerta['titolo']}\n👉 {offerta['link']}"
        canale_id = canali.get(offerta['categoria'])
        if canale_id:
            try:
                bot.send_photo(chat_id=canale_id, photo=offerta['immagine'], caption=messaggio)
                print(f"✅ Inviato a {offerta['categoria']}")
            except Exception as e:
                print(f"❌ Errore su {offerta['categoria']}: {e}")

# Loop ogni 15 minuti
while True:
    invia_offerte()
    time.sleep(900)
