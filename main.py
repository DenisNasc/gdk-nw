import os
from dotenv import load_dotenv
import discord
import discord.utils

from commands.help import handle_help_commands

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_PREFIX = os.getenv("BOT_PREFIX")

CHANNEL_COMO_USAR = os.getenv("CHANNEL_COMO_USAR")

BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Bot(discord.Client):
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        message_content = message.content.lower().strip()
        message_author = message.author
        command = message_content
        param = ""

        if message_author == self.user:
            return

        if not message_content[0] == BOT_PREFIX:
            return

        if len(message_content.split(" ")) > 1:
            command = message_content.split(" ")[0]
            param = message_content.split(" ")[1]

        if command == f"{BOT_PREFIX}help":
            if param:
                await handle_help_commands(message, param)
            else:
                embed = discord.Embed(title="Ajuda", color=discord.Colour.dark_orange())
                embed.description = f"Para receber ajuda específica, digite um dos comandos abaixo. Para saber todos os comandos disponíveis do **Kenner BOT**: `!comandos` \n\n **Regras**: `!help regras`\n**Musicas**: `!help musicas`\n **Cargos**: `!help cargos`"
                embed.set_footer(text="Resposta ao comando: !help")
                reply = await message.channel.send(embed=embed)
                await reply.add_reaction("🆘")

            return

        else:
            embed = discord.Embed(title="Erro de Sintaxe", color=discord.Colour.red())
            embed.description = f"Nenhum comando encontrado.\n\nPara saber todos os comandos disponíveis do **Kenner BOT**, digite: `!comandos`"
            reply = await message.channel.send(embed=embed)
            await reply.add_reaction("❌")

    async def on_raw_reaction_add(self, payload):
        message = await self.get_channel(payload.channel_id).fetch_message(
            payload.message_id
        )
        user = payload.member

        if user == self.user:
            return

        if message.channel.name == "criar-perfil":
            role_visitante = discord.utils.get(user.guild.roles, name=f"Visitante")
            role_colono = discord.utils.get(user.guild.roles, name=f"Colôno")

            message_content = message.content.lower().strip()

            if "**sim, faço parte da gdk**" == message_content:
                await user.add_roles(role_colono)
            elif "**não, sou apenas um visitante**" == message_content:
                await user.add_roles(role_visitante)


client = Bot()
client.run(BOT_TOKEN)
