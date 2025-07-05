iimport time
import requests
from telebot import TeleBot

# Token del bot Telegram
TOKEN = '7267062520:AAHPb1Wy1VbsvZ9qBYO-pbaQ6G7PqQbF_KQ'
bot = TeleBot(TOKEN)

# ID dei canali Telegram
canali = {
    'tech': -1002532953670,
    'casa': -1002768166518,
    'gaming': -1002755987703,
    'offerte': -1002673875319,
    'svapo': -1002523268812
}

# Funzione per recuperare offerte (statico per ora)
def recupera_offerte():
    return [
        {
            'titolo': '🔌 Offerta Tech: Caricatore Anker 20W',
            'link': 'https://www.amazon.it/dp/B08XYXZ12Z?tag=affaritech21-21',
            'immagine': 'https://m.media-amazon.com/images/I/61ixzU4gRPL._AC_SL1500_.jpg',
            'categoria': 'tech'
        },
        {
            'titolo': '🏡 Offerta Casa: Lampada LED Smart Alexa',
            'link': 'https://www.amazon.it/dp/B08KH5R4D2?tag=affaritech21-21',
            'immagine': 'https://m.media-amazon.com/images/I/61aywLfXKjL._AC_SL1500_.jpg',
            'categoria': 'casa'
        },
        {
            'titolo': '🎮 Offerta Gaming: Controller PS4 wireless',
            'link': 'https://www.amazon.it/dp/B08P2D1JZZ?tag=affaritech21-21',
            'immagine': 'https://m.media-amazon.com/images/I/61Ig9vM3ubL._AC_SL1500_.jpg',
            'categoria': 'gaming'
        },
        {
            'titolo': '💥 Super Offerta: Powerbank 20000mAh in sconto!',
            'link': 'https://www.amazon.it/dp/B08T5QXMKK?tag=affaritech21-21',
            'immagine': 'https://m.media-amazon.com/images/I/61IlnP+bYIL._AC_SL1500_.jpg',
            'categoria': 'offerte'
        },
        {
            'titolo': '🔥 SvapoStore: Aroma premium a 2,99€!',
            'link': 'https://www.svapostore.net/liquidi/aroma-premium-vaniglia?tracking=jD7Vnx8Leh2ABPYfEX9LOaSYXtDy6ePBMdWX6kaN5bViiEaB4450Wx2NuOUceDNF',
            'immagine': 'https://www.svapostore.net/modules/ph_simpleblog/covers/300.jpg',
            'categoria': 'svapo'
        }
    ]

# Invia le offerte ogni 60 minuti (puoi cambiare il tempo)
while True:
    offerte = recupera_offerte()
    for offerta in offerte:
        testo = f"{offerta['titolo']}\n👉 {offerta['link']}"
        try:
            bot.send_photo(chat_id=canali[offerta['categoria']], photo=offerta['immagine'], caption=testo)
            print(f"Inviata a {offerta['categoria']}")
        except Exception as e:
            print(f"Errore su {offerta['categoria']}: {e}")
    time.sleep(3600)  # ogni 60 minuti
