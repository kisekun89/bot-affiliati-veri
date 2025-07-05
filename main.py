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

# Esempio di offerte reali (puoi sostituirle o collegarle a un database)
offerte = {
    'tech': {
        'titolo': '💻 HUB USB-C 7in1 in offerta!',
        'link': 'https://www.amazon.it/dp/B0BMYVQXKV?tag=affaritech21-21',
        'prezzo': '💸 Solo 19,99€ invece di 39,99€!',
    },
    'casa': {
        'titolo': '🧼 Set 5 spugne in microfibra lavabili',
        'link': 'https://www.amazon.it/dp/B08CXXF8TL?tag=affaritech21-21',
        'prezzo': '💸 6,49€ spedizione Prime',
    },
    'gaming': {
        'titolo': '🎮 Controller PS4 Wireless',
        'link': 'https://www.amazon.it/dp/B07W6JD6W5?tag=affaritech21-21',
        'prezzo': '💸 24,99€ con sconto reale',
    },
    'offerte': {
        'titolo': '🛍️ Zaino antifurto impermeabile',
        'link': 'https://www.amazon.it/dp/B07H7NHF5N?tag=affaritech21-21',
        'prezzo': '💸 Solo 15,99€!',
    },
    'svapo': {
        'titolo': '🔥 Liquido Svapo Super Flavor Madagascar 10ml',
        'link': 'https://www.svapostore.net/liquidi-fai-da-te/super-flavor-aroma-madagascar-10ml?tracking=jD7Vnx8Leh2ABPYfEX9LOaSYXtDy6ePBMdWX6kaN5bViiEaB4450Wx2NuOUceDNF',
        'prezzo': '💨 Solo 4,90€ su SvapoStore!',
    }
}

# Funzione per inviare i messaggi
def invia_offerte():
    for categoria, chat_id in canali.items():
        try:
            offerta = offerte.get(categoria)
            if offerta:
                messaggio = f"{offerta['titolo']}\n\n{offerta['prezzo']}\n🔗 {offerta['link']}"
                bot.send_message(chat_id, messaggio)
                print(f"✅ Inviato a {categoria}")
            else:
                print(f"⚠️ Nessuna offerta per {categoria}")
        except Exception as e:
            print(f"❌ Errore su {categoria}: {e}")

# Ciclo infinito ogni 15 minuti (modificabile)
if __name__ == "__main__":
    while True:
        invia_offerte()
        time.sleep(900)  # 900 secondi = 15 minuti
