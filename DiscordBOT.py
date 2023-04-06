import discord
import openai
import os

DISCORD_BOT_TOKEN = 'YOUR_DISCORD_BOT_TOKEN_HERE'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY_HERE'

client = discord.Client()
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

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_message = message.content
    response = generate_response(user_message)

    await message.channel.send(response)

client.run(DISCORD_BOT_TOKEN)
