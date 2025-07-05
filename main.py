import time
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

# Funzione che restituisce offerte simulate
def recupera_offerte():
    return [
        {
            'titolo': 'Caricatore USB-C 20W in super offerta!',
            'link': 'https://www.amazon.it/dp/B09XXYZ12Z?tag=affaritech21-21',
            'categoria': 'tech'
        },
        {
            'titolo': 'Liquido Svapo Vaniglia 10ml a 2,99€',
            'link': 'https://www.svapostore.net/liquidi/aroma-vaniglia?tracking=jD7Vnx8Leh2A',
            'categoria': 'svapo'
        }
    ]

# Invio ogni 15 minuti
while True:
    offerte = recupera_offerte()
    for offerta in offerte:
        canale_id = canali.get(offerta['categoria'])
        if canale_id:
            messaggio = f"🔥 {offerta['titolo']}\n👉 {offerta['link']}"
            try:
                bot.send_message(canale_id, messaggio, disable_web_page_preview=True)
                print(f"✅ Inviato a {offerta['categoria']}")
            except Exception as e:
                print(f"❌ Errore su {offerta['categoria']}: {e}")
    time.sleep(900)  # ogni 15 minuti
