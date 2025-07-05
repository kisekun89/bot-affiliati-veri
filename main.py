import telebot
import requests
import os
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CANALI = os.getenv("CANALI").split(",")
FREQUENZA_MINUTI = int(os.getenv("FREQUENZA_MINUTI", 60))
AFFILIATE_ID = os.getenv("AFFILIATE_ID")
DISCLAIMER = os.getenv("DISCLAIMER", "")
GLITCH_TAG = os.getenv("GLITCH_TAG", "")
SVAPO_TRACKING = os.getenv("SVAPO_TRACKING")
SVAPO_URL_BASE = os.getenv("SVAPO_URL_BASE")

bot = telebot.TeleBot(BOT_TOKEN)

def recupera_offerte():
    # Simulazione dati (da sostituire con scraping o API vere)
    return [
        {
            "titolo": "🔥 Offerta Imperdibile Amazon",
            "prezzo": "19,99€",
            "immagine": "https://m.media-amazon.com/images/I/81vpsIs58WL._AC_SL1500_.jpg",
            "link": f"https://www.amazon.it/dp/B08N5WRWNW?tag={AFFILIATE_ID}",
            "glitch": True
        },
        {
            "titolo": "💨 Liquido Svapo Top",
            "prezzo": "4,90€",
            "immagine": "https://www.svapostore.net/img/p/7/1/5/3/7153-large_default.jpg",
            "link": f"{SVAPO_URL_BASE}/liquido-top?tracking={SVAPO_TRACKING}",
            "glitch": False
        }
    ]

def immagine_valida(url):
    try:
        response = requests.head(url)
        return response.status_code == 200 and "image" in response.headers.get("content-type", "")
    except:
        return False

def formatta_messaggio(offerta):
    messaggio = f"🛒 <b>{offerta['titolo']}</b>\n"
    messaggio += f"💰 <b>Prezzo:</b> {offerta['prezzo']}\n"
    if offerta['glitch']:
        messaggio += f"{GLITCH_TAG}\n"
    messaggio += f"🔗 <a href=\"{offerta['link']}\">Acquista ora</a>\n\n"
    messaggio += DISCLAIMER
    return messaggio

def invia_offerta(canale, offerta):
    messaggio = formatta_messaggio(offerta)
    immagine = offerta.get("immagine")

    if immagine and immagine_valida(immagine):
        try:
            bot.send_photo(
                chat_id=canale.strip(),
                photo=immagine,
                caption=messaggio,
                parse_mode="HTML"
            )
        except Exception as e:
            print(f"Errore invio foto su {canale}: {e}")
            bot.send_message(
                chat_id=canale.strip(),
                text=messaggio,
                parse_mode="HTML",
                disable_web_page_preview=True
            )
    else:
        bot.send_message(
            chat_id=canale.strip(),
            text=messaggio,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

def invia_tutte_le_offerte():
    offerte = recupera_offerte()
    for canale in CANALI:
        for offerta in offerte:
            invia_offerta(canale, offerta)

if __name__ == "__main__":
    while True:
        invia_tutte_le_offerte()
        time.sleep(FREQUENZA_MINUTI * 60)
