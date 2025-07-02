# 🔹 Step 1: Clone the repo
!git clone https://github.com/nakul0405/Alexa-V2.git
%cd Alexa-V2

# 🔹 Step 2: Install requirements
!pip install -r requirements.txt
!pip install python-telegram-bot

# 🔹 Step 3: Create run_bot.py file
code = '''
import logging
from telegram.ext import Updater, MessageHandler, Filters
from alexa.chat import alexa_response  # main Alexa logic

# Logging setup
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Set up token from env
import os
TOKEN = os.getenv("7769164684:AAEbmD6Y7QpWyCBKPQGAsfWfWjaV-76NKxo")

if TOKEN is None:
    raise Exception("7769164684:AAEbmD6Y7QpWyCBKPQGAsfWfWjaV-76NKxo environment variable not set.")

# Handle user message
def handle_message(update, context):
    user_text = update.message.text
    response = alexa_response(user_text)  # call to alexa/chat.py
    update.message.reply_text(response)

# Main loop
def main():
    updater = Updater(token=7769164684:AAEbmD6Y7QpWyCBKPQGAsfWfWjaV-76NKxo, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
'''
with open("run_bot.py", "w") as f:
    f.write(code)

# 🔹 Step 4: Set your Telegram bot token here
import os
os.environ['TELEGRAM_TOKEN'] = '7769164684:AAEbmD6Y7QpWyCBKPQGAsfWfWjaV-76NKxo'  # 🔁 Replace this with your actual token

# 🔹 Step 5: Run the bot
!python run_bot.py
