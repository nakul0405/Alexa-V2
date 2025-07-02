import logging
from telegram.ext import Updater, MessageHandler, Filters
from alexa.chat import alexa_response  # importing from repo

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your Telegram Bot Token
import os
TOKEN = os.getenv("7769164684:AAEbmD6Y7QpWyCBKPQGAsfWfWjaV-76NKxo")

if TOKEN is None:
    raise Exception("7769164684:AAEbmD6Y7QpWyCBKPQGAsfWfWjaV-76NKxo environment variable not set.")

# Function to handle incoming messages
def handle_message(update, context):
    user_text = update.message.text
    response = alexa_response(user_text)  # Call Alexa-V2 core function
    update.message.reply_text(response)

# Main function
def main():
    updater = Updater(token=7769164684:AAEbmD6Y7QpWyCBKPQGAsfWfWjaV-76NKxo, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()
import 
os.environ['TELEGRAM_TOKEN'] = '7769164684:AAEbmD6Y7QpWyCBKPQGAsfWfWjaV-76NKxo'

if __name__ == '__main__':
    main()
