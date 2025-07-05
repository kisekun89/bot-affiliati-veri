import time
import requests
from telebot import TeleBot

# TOKEN del tuo bot
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

# Offerte reali testate
offerte = {
    'tech': {
        'titolo': '🔌 Caricatore USB-C 20W per iPhone',
        'prezzo': '💰 Solo 9,99€',
        'link': 'https://www.amazon.it/dp/B08ZJQ3Y2N?tag=affaritech21-21'
    },
    'casa': {
        'titolo': '💡 Striscia LED RGB 5m con telecomando',
        'prezzo': '💰 7,99€',
        'link': 'https://www.amazon.it/dp/B0B5MB98HV?tag=affaritech21-21'
    },
    'gaming': {
        'titolo': '🎮 Supporto cuffie RGB Trust',
        'prezzo': '💰 19,90€',
        'link': 'https://www.amazon.it/dp/B09ND5Q7YT?tag=affaritech21-21'
    },
    'offerte': {
        'titolo': '🛏️ Set 2 cuscini memory foam 50x80',
        'prezzo': '💰 24,90€',
        'link': 'https://www.amazon.it/dp/B07VV47Z7L?tag=affaritech21-21'
    },
    'svapo': {
        'titolo': '💨 Elfbar ELFX Pro Pod Kit (SvapoStore)',
        'prezzo': '💰 12,90€',
        'link': 'https://www.svapostore.net/kit-sigarette-elettroniche/elfbar-elfx-pro-pod-kit?tracking=jD7Vnx8Leh2ABPYfEX9LOaSYXtDy6ePBMdWX6kaN5bViiEaB4450Wx2NuOUceDNF'
    }
}

# Invio messaggi
for categoria, dati in offerte.items():
    messaggio = f"{dati['titolo']}\n{dati['prezzo']}\n👉 {dati['link']}"
    try:
        bot.send_message(canali[categoria], messaggio)
        print(f"Inviato a {categoria}")
    except Exception as e:
        print(f"Errore su {categoria}: {e}")
