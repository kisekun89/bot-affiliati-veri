import time
import requests
from telebot import TeleBot

# Inserisci il token del tuo bot qui
TOKEN = '7267062520:AAHPb1Wy1VbsvZ9qBYO-pbaQ6G7PqQbF_KQ'
bot = TeleBot(TOKEN)

# ID dei tuoi canali Telegram
canali = {
    'tech': -1002532953670,
    'casa': -1002768166518,
    'gaming': -1002755987703,
    'offerte': -1002673875319,
    'svapo': -1002523268812
}

# Offerte da inviare (puoi ampliarle)
def recupera_offerte():
    return [
        {
            'titolo': '🔌 Offerta Tech: Caricatore USB-C 20W',
            'link': 'https://www.amazon.it/dp/B09XXYZ12Z?tag=affaritech21-21',
            'immagine': 'https://m.media-amazon.com/images/I/61ixPBLqW-L._AC_SL1500_.jpg',
            'categoria': 'tech'
        },
        {
            'titolo': '💨 Offerta Svapo: Aroma Premium alla Vaniglia',
            'link': 'https://www.svapostore.net/liquidi/aroma-vaniglia?tracking=jD7Vnx8Leh2ABPYfEX9LOaSYXtDy6ePBMdWX6kaN5bViiEaB4450Wx2NuOUceDNF',
            'immagine': 'https://www.svapostore.net/media/catalog/product/cache/4/image/800x800/9df78eab33525d08d6e5fb8d27136e95/a/r/aroma-vaniglia.jpg',
            'categoria': 'svapo'
        }
    ]

# Invio automatico
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
    time.sleep(900)  # 15 minuti (900 secondi)
