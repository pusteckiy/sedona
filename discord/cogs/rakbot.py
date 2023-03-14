import requests

import discord
from discord import app_commands
from discord.ext import commands

from settings import API_TOKEN, GUILD_ID, ADMIN_ROLE_ID
from service import forms

API_URL = 'https://cyber-sedona.fun/api/'

headers = {
    'Authorization': f'Token {API_TOKEN}',
}

class RakBot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.hybrid_command(name='form', with_app_command=True, description='Проверит `form` и отправит на обработку.')
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def check_and_save_form(self, ctx: discord.Message, *, form: str):
        if ADMIN_ROLE_ID not in [role.id for role in ctx.author.roles]:
            return await ctx.reply('**:warning: Отсутствует доступ.**')

        valid_commands, invalid_commands = forms.check_forms(form.split('\n'))
        for command in valid_commands:
            requests.post(API_URL + 'rak-bot/command', headers=headers, data={'text': command})
        valid_forms = forms.make_results(valid_commands, '**Одобрены:**')
        invalid_forms = forms.make_results(invalid_commands, '\n**Ошибочные:**')
        await ctx.reply(embed=discord.Embed(description=valid_forms+invalid_forms, color=discord.Color.dark_blue()))


    @commands.hybrid_command(name='command', with_app_command=True, description='Напишет в чат текст с `command`')
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def send_command_to_chat(self, ctx: discord.Message, *, command: str):
        if ADMIN_ROLE_ID not in [role.id for role in ctx.author.roles]:
            return await ctx.reply('**:warning: Отсутствует доступ.**')

        response = requests.post(API_URL + 'rak-bot/command', headers=headers, data={'text': command}).json()
        await ctx.reply(f'**:ghost: {response["message"]}**')
    

    @commands.hybrid_command(name='getforms', with_app_command=True, description='Отправит список актуальных для выдачи форм.')
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def get_list_of_forms(self, ctx: discord.Message):
        if ADMIN_ROLE_ID not in [role.id for role in ctx.author.roles]:
            return await ctx.reply('**:warning: Отсутствует доступ.**')
        
        response = requests.get(API_URL + 'rak-bot/command', headers=headers).json()
        command_list = [f"{command['id']} | {command['text']}" for command in response['commands']]
        text = forms.make_results(command_list, '')
        await ctx.reply(embed=discord.Embed(title='На выдаче:', description=text, color=discord.Color.dark_blue()))


    @commands.hybrid_command(name='dform', with_app_command=True, description='Удалит форму по указанному `id`. Можно указывать несколько через пробел.')
    @app_commands.guilds(discord.Object(id=GUILD_ID))
    async def accept_form_by_id(self, ctx: discord.Message, *, command_id):
        if ADMIN_ROLE_ID not in [role.id for role in ctx.author.roles]:
            return await ctx.reply('**:warning: Отсутствует доступ.**')
        
        ids = command_id.split(' ')
        int_ids = map(int, ids)
        for _id in int_ids:
            response = requests.patch(API_URL + 'rak-bot/command',data={'id': _id}, headers=headers).json()
            await ctx.reply(f'**:ghost: {_id} | {response["message"]}**')



async def setup(bot):
    await bot.add_cog(RakBot(bot), guilds=[discord.Object(id=GUILD_ID)])
