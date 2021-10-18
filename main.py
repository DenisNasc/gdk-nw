from dotenv import dotenv_values
import discord

config = dotenv_values(dotenv_path=".env")
BOT_TOKEN = config["BOT_TOKEN"]


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
