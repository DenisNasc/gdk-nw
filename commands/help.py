import discord


async def handle_help_commands(message: discord.Message, param: str):
    if param == "regras":
        embed = discord.Embed(
            title="Ajuda | Regras", color=discord.Colour.dark_orange()
        )
        embed.description = f""
        embed.set_footer(text="Resposta ao comando: !help regras")
        reply = await message.channel.send(embed=embed)
        await reply.add_reaction("🆘")

    elif param == "musicas":
        embed = discord.Embed(
            title="Ajuda | Musicas", color=discord.Colour.dark_orange()
        )
        embed.description = f""
        embed.set_footer(text="Resposta ao comando: !help musicas")
        reply = await message.channel.send(embed=embed)
        await reply.add_reaction("🆘")

    elif param == "cargos":
        embed = discord.Embed(
            title="Ajuda | Cargos", color=discord.Colour.dark_orange()
        )
        embed.description = f""
        embed.set_footer(text="Resposta ao comando: !help cargos")
        reply = await message.channel.send(embed=embed)
        await reply.add_reaction("🆘")

    else:
        pass
