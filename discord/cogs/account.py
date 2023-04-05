import requests

import discord
from discord import app_commands
from discord.ext import commands

from settings import API_TOKEN, GUILD_ID


API_URL = 'https://cyber-sedona.fun/api'

headers = {
    'Authorization': f'Token {API_TOKEN}',
}


class Account(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name='me', with_app_command=True, description='Получить информацию с профиля.')
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def get_account(self, ctx: discord.Message):
        response = requests.get(
            API_URL + f'/account/{ctx.author.id}', headers=headers).json()
        if response.get('status') == 'error':
            return await ctx.reply('**:eyes: Аккаунт не найден**')
        embed = discord.Embed(title=response.get('nickname'),
                              description=f"На счету: {response.get('money')}\nSC: {response.get('coins')}",
                              color=discord.Color.dark_blue())
        return await ctx.reply(embed=embed)

    @commands.hybrid_command(name='rakbot', with_app_command=True, description='Снять ракбота с аккаунта.')
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def clear_rakbot(self, ctx: discord.Message):
        response = requests.get(
            API_URL + f'/account/{ctx.author.id}', headers=headers).json()
        if response.get('status') == 'error':
            return await ctx.reply('**:eyes: Аккаунт не найден**')
        if response.get('nickname') == None:
            return await ctx.reply('**:eyes: Сначала привяжите аккаунт к сайту.**')
        return await ctx.reply('Заглушка.')


async def setup(bot):
    await bot.add_cog(Account(bot), guilds=[discord.Object(id=GUILD_ID)])
