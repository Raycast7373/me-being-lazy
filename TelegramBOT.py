import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
import os

TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY_HERE'

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
openai.api_key = OPENAI_API_KEY

def generate_response(user_message):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"User: {user_message}\nAI:",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm a chatbot powered by OpenAI's GPT-3 language model. How can I assist you today?")

def handle_message(update, context):
    user_message = update.message.text
    response = generate_response(user_message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.start_polling()
updater.idle()
