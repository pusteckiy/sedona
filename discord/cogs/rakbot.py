import requests
import asyncio

import discord
from discord import app_commands
from discord.ext import commands

from settings import API_TOKEN, GUILD_ID, MANAGEMENT_ADMIN_ROLE_ID, LVL_4_ADMIN_ROLE_ID
from service import forms, check

API_URL = 'https://cyber-sedona.fun/api'

headers = {
    'Authorization': f'Token {API_TOKEN}',
}


class RakBot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name='form', with_app_command=True, description='Проверит `form` и отправит на обработку.')
    @commands.has_any_role(MANAGEMENT_ADMIN_ROLE_ID)
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def check_and_save_form(self, ctx: discord.Message, *, form: str):
        valid_commands, invalid_commands = forms.check_forms(form.split('\n'))
        for command in valid_commands:
            requests.post(API_URL + '/rak-bot/command',
                          headers=headers, data={'text': command})
        valid_forms = forms.make_results(valid_commands, '**Одобрены:**')
        invalid_forms = forms.make_results(
            invalid_commands, '\n**Ошибочные:**')
        await ctx.reply(embed=discord.Embed(description=valid_forms+invalid_forms, color=discord.Color.dark_blue()))

    @commands.hybrid_command(name='command', with_app_command=True, description='Напишет в чат текст с `command`')
    @commands.has_any_role(MANAGEMENT_ADMIN_ROLE_ID)
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def send_command_to_chat(self, ctx: discord.Message, *, command: str):
        response = requests.post(
            API_URL + '/rak-bot/command', headers=headers, data={'text': command}).json()
        await ctx.reply(f"**:ghost: Запрос №{response['id']} отправлен на обработку.**")

    @commands.hybrid_command(name='getforms', with_app_command=True, description='Отправит список актуальных для выдачи форм.')
    @commands.has_any_role(MANAGEMENT_ADMIN_ROLE_ID)
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def get_list_of_forms(self, ctx: discord.Message):
        response = requests.get(
            API_URL + '/rak-bot/command', headers=headers).json()
        command_list = [
            f"{command['id']} | {command['text']}" for command in response]
        text = forms.make_results(command_list, '')
        await ctx.reply(embed=discord.Embed(title='На выдаче:', description=text, color=discord.Color.dark_blue()))

    @commands.hybrid_command(name='check', with_app_command=True, description='Получить статистику игрока.')
    @commands.has_any_role(MANAGEMENT_ADMIN_ROLE_ID, LVL_4_ADMIN_ROLE_ID)
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def get_list_of_forms(self, ctx: discord.Message, *, username: str):
        response = requests.post(
            API_URL + '/rak-bot/checkoff', params={'username': username}, headers=headers).json()
        message = await ctx.reply(f'**:ghost: Запрос №{response["id"]} обрабатывается..**')
        await asyncio.sleep(4)
        response = requests.get(
            API_URL + f'/rak-bot/command/{response["id"]}', headers=headers).json()
        player = response['response']
        title, description = check.form_player_stats_answer(player)
        embed = discord.Embed(
            title=title, color=discord.Color.dark_blue(), description=description)
        embed.set_footer(text=f"Запрос №{response['id']} от [{ctx.author.id}]")
        await message.edit(content='', embed=embed)


async def setup(bot):
    await bot.add_cog(RakBot(bot), guilds=[discord.Object(id=GUILD_ID)])
