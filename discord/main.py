import discord
from discord.ext import commands
from settings import TOKEN, GUILD_ID


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=discord.Intents.all(),
            application_id = 821736713231007765)
    
    async def setup_hook(self):
        await self.load_extension('cogs.rakbot')
        await self.load_extension('cogs.account')
        await bot.tree.sync(guild = discord.Object(id=GUILD_ID))

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingAnyRole):
            embed = discord.Embed(title='Ошибка!', description=':warning: Отсутствует нужный доступ.', color=discord.Color.red())

        if not isinstance(error, commands.CommandNotFound):
            embed = discord.Embed(title='Ошибка!', description=str(error), color=discord.Color.red())
            await ctx.reply(embed=embed, ephemeral=True)

    async def on_ready(self):
        print(f'{self.user} успішно запущений.')


bot = Bot()
bot.remove_command('help')
bot.run(TOKEN)
