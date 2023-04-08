from aiogram import Bot, Dispatcher, executor, types
import openai
import os

TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY_HERE'

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)
openai.api_key = OPENAI_API_KEY

def generate_response(user_message):
    ai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lemessage,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return ai_response.choices[0].message.content.strip()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Hi! I'm a chatbot powered by OpenAI's GPT-3 language model. How can I assist you today?")

@dp.message_handler()
async def chatgpt(message: types.Message):
    user_message = message.text
    user = message.from_user.full_name
    print(user_message)
    print(user)
    dumessage = f'{user}: {user_message}'
    lemessage = [{"role": "user", "content": dumessage}]
    ai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lemessage,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = ai_response.choices[0].message.content.strip()
    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
