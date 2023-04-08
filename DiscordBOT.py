import discord
import openai
import os

DISCORD_BOT_TOKEN = 'YOUR_DISCORD_BOT_TOKEN_HERE'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY_HERE'

intents = discord.Intents(messages=True, message_content=True)
bot = discord.Client(intents=intents)
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

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    user = ctx.author
    user_message = ctx.content
    channel = ctx.channel
    dumessage = f'{user}: {user_message}'
    lemessage = [{"role": "user", "content": dumessage}]
    async with channel.typing():    
        ai_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=lemessage,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        response = ai_response.choices[0].message.content.strip()
        await ctx.channel.send(response)

bot.run(DISCORD_BOT_TOKEN)
