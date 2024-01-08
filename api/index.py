from flask import Flask
import discord
from discord.ext import tasks
from dhooks import Webhook
import os
import nextcord
from nextcord.ext import commands
import asyncio
from requests import post

app = Flask(__name__)
hook = Webhook('https://discord.com/api/webhooks/1194012870078378054/eevDHgzT9OGSehwGUDyYzXhZZtZhkYB4_w_rx4lg_AVFyMbAQOudZEgtxAdQhVGXKgfx')

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(intents=intents,command_prefix='!')
bot_token = 'MTE5MDgyMjIxOTE3NDEyOTcyNQ.GZ1A2M.eBvP7N3oW3FUIS7AicmI9Gyi9MoeK6EinW8hRM'

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('!send_message'):
        hook.send('Message sent from Discord bot!')




@app.route('/')
def hello():
    hook.send('Hello from Flask!')
    return 'Hello, world'

def run():
    bot.loop.create_task(bot.start(bot_token))
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    bot.run(bot_token)
    run()
