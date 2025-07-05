import telebot
import os
import time
import random

BOT_TOKEN = os.getenv("BOT_TOKEN")
CANALI = os.getenv("CANALI", "").split(",")
FREQUENZA_MINUTI = int(os.getenv("FREQUENZA_MINUTI", "15"))

LINK_SVAPO = os.getenv("LINK_SVAPO", "https://www.svapostore.net/?tracking=jD7Vnx8Leh2ABPYfEX9LOaSYXtDy6ePBMdWX6kaN5bViiEaB4450Wx2NuOUceDNF")

OFFERTE = {
    "tech": [
        {
            "titolo": "Powerbank 20000mAh 🔋",
            "prezzo": "14,99€",
            "link": "https://www.amazon.it/dp/B08XMBLKR2?tag=affaritech21-21"
        },
        {
            "titolo": "SSD 1TB Crucial 🚀",
            "prezzo": "49,99€",
            "link": "https://www.amazon.it/dp/B08GY8N1HR?tag=affaritech21-21"
        }
    ],
    "casa": [
        {
            "titolo": "Lampada LED RGB 🌈",
            "prezzo": "11,99€",
            "link": "https://www.amazon.it/dp/B07ZVKTP53?tag=affaritech21-21"
        },
        {
            "titolo": "Profumo uomo 100ml 🔥",
            "prezzo": "19,90€",
            "link": "https://www.amazon.it/dp/B08N5WRWNW?tag=affaritech21-21"
        }
    ],
    "nerd": [
        {
            "titolo": "Controller PS5 🎮",
            "prezzo": "49,99€",
            "link": "https://www.amazon.it/dp/B08H99BPJN?tag=affaritech21-21"
        },
        {
            "titolo": "Funko Pop One Piece 🏴‍☠️",
            "prezzo": "14,00€",
            "link": "https://www.amazon.it/dp/B07P7S2F1J?tag=affaritech21-21"
        }
    ],
    "svapo": [
        {
            "titolo": "🔥 Offerta SvapoStore",
            "prezzo": "Aroma premium a 2,99€",
            "link": LINK_SVAPO
        }
    ]
}

bot = telebot.TeleBot(BOT_TOKEN)

def scegli_categoria(canale):
    if "tech" in canale:
        return "tech"
    elif "casa" in canale:
        return "casa"
    elif "manga" in canale or "gaming" in canale:
        return "nerd"
    elif "svapo" in canale:
        return "svapo"
    else:
        return random.choice(["tech", "casa", "nerd"])

def invia_offerta(canale):
    categoria = scegli_categoria(canale)
    offerta = random.choice(OFFERTE[categoria])
    messaggio = f"🛒 {offerta['titolo']}
💰 {offerta['prezzo']}
🔗 {offerta['link']}"
    try:
        bot.send_message(canale.strip(), messaggio)
        print(f"✅ Inviato su {canale}")
    except Exception as e:
        print(f"❌ Errore su {canale}: {e}")

while True:
    for canale in CANALI:
        invia_offerta(canale)
    time.sleep(FREQUENZA_MINUTI * 15)
