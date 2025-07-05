import time
import requests
from telebot import TeleBot

# TOKEN del bot Telegram
TOKEN = '7267062520:AAHPb1Wy1VbsvZ9qBYO-pbaQ6G7PqQbF_KQ'
bot = TeleBot(TOKEN)

# ID dei canali Telegram (con -100 davanti)
canali = {
    'tech': -1002532953670,
    'casa': -1002768166518,
    'gaming': -1002755987703,
    'offerte': -1002673875319,
    'svapo': -1002523268812
}

# Funzione che simula il recupero delle offerte (da sostituire con scraping/API)
def recupera_offerte():
    return [
        {
            'titolo': '🔌 Offerta Tech: Caricatore USB-C 20W',
            'link': 'https://www.amazon.it/dp/B09XXYZ12Z?tag=affaritech21-21',
            'immagine': 'https://m.media-amazon.com/images/I/61xyz.jpg',
            'categoria': 'tech'
        },
        {
            'titolo': '🏡 Offerta Casa: Lampada LED da Comodino',
            'link': 'https://www.amazon.it/dp/B08XYZL456?tag=affaritech21-21',
            'immagine': 'https://m.media-amazon.com/images/I/81abc.jpg',
            'categoria': 'casa'
        },
        {
            'titolo': '🎮 Offerta Gaming: Controller PS5',
            'link': 'https://www.amazon.it/dp/B09GXYZ123?tag=affaritech21-21',
            'immagine': 'https://m.media-amazon.com/images/I/91gamepad.jpg',
            'categoria': 'gaming'
        },
        {
            'titolo': '🔥 Offerta Varie: Sconto top su prodotti scelti!',
            'link': 'https://www.amazon.it/dp/B09VXYZ789?tag=affaritech21-21',
            'immagine': 'https://m.media-amazon.com/images/I/91random.jpg',
            'categoria': 'offerte'
        },
        {
            'titolo': '💨 Offerta Svapo: Aroma Premium alla Vaniglia',
            'link': 'https://www.svapostore.net/liquidi/aroma-vaniglia?tracking=jD7Vnx8Leh2ABPYfEX9LOaSYXtDy6ePBMdWX6kaN5bViiEaB4450Wx2NuOUceDNF',
            'immagine': 'https://www.svapostore.net/media/aroma-vaniglia.jpg',
            'categoria': 'svapo'
        }
    ]

# Funzione per inviare le offerte nei canali
def invia_offerte():
    offerte = recupera_offerte()
    for offerta in offerte:
        messaggio = f"{offerta['titolo']}\n👉 {offerta['link']}"
        immagine = offerta['immagine']
        categoria = offerta['categoria']

        try:
            bot.send_photo(chat_id=canali[categoria], photo=immagine, caption=messaggio)
            print(f"Inviata offerta a {categoria}")
        except Exception as e:
            print(f"Errore nell'invio a {categoria}: {e}")

# Esegui ogni 15 minuti
while True:
    invia_offerte()
    time.sleep(900)  # 15 minuti (900 secondi)
