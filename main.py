import time
import requests
from telebot import TeleBot

# Token del tuo bot Telegram
TOKEN = '7267062520:AAHPb1Wy1VbsvZ9qBYO-pbaQ6G7PqbF_KQ'
bot = TeleBot(TOKEN)

# ID canali Telegram
canali = {
    'tech': -1002532953670,
    'casa': -1002768166518,
    'gaming': -1002755987703,
    'offerte': -1002673875319,
    'svapo': -1002523268812
}

# Offerte reali
def recupera_offerte():
    return [
        {
            'titolo': '🔋 Caricatore USB-C 20W in offerta!',
            'link': 'https://www.amazon.it/dp/B0BJY6SXPX?tag=affaritech21-21',
            'categoria': 'tech'
        },
        {
            'titolo': '💨 Aroma Svapo Madagascar 10ml a prezzo bomba!',
            'link': 'https://www.svapostore.net/liquidi-fai-da-te/super-flavor-aroma-madagascar-10ml?tracking=jD7Vnx8Leh2ABPYfEX9LOaSYXtDy6ePBMdWX6kaN5bViiEaB4450Wx2NuOUceDNF',
            'categoria': 'svapo'
        }
    ]

while True:
    offerte = recupera_offerte()
    for offerta in offerte:
        canale_id = canali.get(offerta['categoria'])
        if canale_id:
            messaggio = f"{offerta['titolo']}\n👉 {offerta['link']}"
            try:
                bot.send_message(canale_id, messaggio, disable_web_page_preview=True)
                print(f"✅ Inviato a {offerta['categoria']}")
            except Exception as e:
                print(f"❌ Errore su {offerta['categoria']}: {e}")
    time.sleep(900)  # ogni 15 minuti
