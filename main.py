import telebot
import requests
import time
import os

BOT_TOKEN = os.environ.get('BOT_TOKEN')
CANALI = os.environ.get('CANALI').split(',')
FREQUENZA_MINUTI = int(os.environ.get('FREQUENZA_MINUTI', 15))
DISCLAIMER = os.environ.get('DISCLAIMER', '')
GLITCH_TAG = os.environ.get('GLITCH_TAG', '')
SVAPO_TRACKING = os.environ.get('SVAPO_TRACKING', '')
SVAPO_URL_BASE = os.environ.get('SVAPO_URL_BASE', 'https://www.svapostore.net')

bot = telebot.TeleBot(BOT_TOKEN)

def get_offerte_amazon():
    # Simulazione offerte Amazon (da sostituire con chiamata reale al tuo sistema)
    return [
        {
            'titolo': 'Cuffie Bluetooth Noise Cancelling',
            'prezzo': '59,99€ (-40%)',
            'link': 'https://www.amazon.it/dp/B09XXXXXXX?tag=affaritech21-21',
            'immagine': 'https://m.media-amazon.com/images/I/71XXXXXXX.jpg'
        }
    ]

def get_offerte_svapo():
    return [
        {
            'titolo': 'Elfbar ELFX PRO Pod Kit',
            'prezzo': '19,90€',
            'link': f'{SVAPO_URL_BASE}/kit-sigarette-elettroniche/elfbar-elfx-pro-pod-kit?tracking={SVAPO_TRACKING}',
            'immagine': 'https://www.svapostore.net/img/cms/elfbar-elfx-pro.jpg'
        }
    ]

def invia_offerta(canale, offerta):
    try:
        messaggio = f"🛒 {offerta['titolo']}\n💰 {offerta['prezzo']}\n🔗 {offerta['link']}\n\n{DISCLAIMER}"
        bot.send_photo(chat_id=canale, photo=offerta['immagine'], caption=messaggio)
        print(f"✅ Inviato su {canale}")
    except Exception as e:
        print(f"❌ Errore su {canale}: {e}")

def ciclo_pubblicazione():
    while True:
        offerte_amazon = get_offerte_amazon()
        offerte_svapo = get_offerte_svapo()

        for canale in CANALI:
            if 'svapo' in canale:
                for offerta in offerte_svapo:
                    invia_offerta(canale, offerta)
            else:
                for offerta in offerte_amazon:
                    invia_offerta(canale, offerta)

        print(f"⏱ Atteso prossima pubblicazione...")
        time.sleep(FREQUENZA_MINUTI * 60)

if __name__ == "__main__":
    ciclo_pubblicazione()
