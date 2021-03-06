import os
from dotenv import load_dotenv
import discord

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == "ping":
            await message.channel.send("pong")


client = MyClient()
client.run(BOT_TOKEN)
