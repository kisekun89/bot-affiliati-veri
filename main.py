import time
import requests
from telebot import TeleBot

# TOKEN del bot Telegram
TOKEN = 'INSERISCI_IL_TUO_TOKEN'
bot = TeleBot(TOKEN)

# Chat ID dei canali Telegram associati
canali = {
    'tech': -1000000000001,
    'casa': -1000000000002,
    'gaming': -1000000000003,
    'offerte': -1000000000004,
    'svapo': -1000000000005
}

# Funzione che recupera le offerte (esempio statico, da sostituire con scraping o API)
def recupera_offerte():
    return [
        {
            'titolo': 'Offerta Tech: Caricatore USB-C 20W',
            'link': 'https://www.amazon.it/dp/B09XXXYZ12?tag=affaritech21-21',
            'immagine': 'https://m.media-amazon.com/images/I/61xyz.jpg',
            'categoria': 'tech'
        },
        {
            'titolo': 'Liquido Svapo alla Vaniglia',
            'link': 'https://www.svapostore.net/liquidi/aroma-vaniglia?tracking=jD7Vnx8Leh2A',
            'immagine': '',
            'categoria': 'svapo'
        }
    ]

# Ciclo principale di pubblicazione
def pubblica_offerte():
    offerte = recupera_offerte()
    for offerta in offerte:
        categoria = offerta['categoria']
        titolo = offerta['titolo']
        link = offerta['link']
        immagine = offerta['immagine']

        messaggio = f"<b>{titolo}</b>\n\n🔗 {link}"

        for nome_canale, chat_id in canali.items():
            if nome_canale == categoria:
                try:
                    if 'svapostore.net' in link or immagine == '':
                        bot.send_message(chat_id, messaggio, parse_mode='HTML')
                    else:
                        bot.send_photo(chat_id, photo=immagine, caption=messaggio, parse_mode='HTML')
                    print(f"✅ Inviato su {nome_canale}")
                except Exception as e:
                    print(f"❌ Errore su {nome_canale}: {e}")

# Loop ogni 15 minuti
if __name__ == '__main__':
    while True:
        pubblica_offerte()
        time.sleep(900)  # 900 secondi = 15 minuti
