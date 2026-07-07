import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def setup(ctx):
    if not ctx.author.guild_permissions.administrator:
        return

    embed = discord.Embed(
        title="✨ ВЕРИФИКАЦИЯ SECO", 
        description="Добро пожаловать! Нажми кнопку ниже, чтобы подтвердить участие и получить доступ к каналам.",
        color=0x2b2d31
    )
    embed.add_field(name="📜 Правила", value="Уважение и адекватность — залог нашего комьюнити.", inline=False)
    
    button = discord.ui.Button(label="ПРОЙТИ ВЕРИФИКАЦИЮ", style=discord.ButtonStyle.primary, emoji="🛡️")

    async def button_callback(interaction: discord.Interaction):
        # ID роли "Участник"
        role = discord.utils.get(interaction.guild.roles, id=1523339212517019729)
        if role:
            await interaction.user.add_roles(role)
            await interaction.response.send_message("Доступ открыт!", ephemeral=True)
        else:
            await interaction.response.send_message("Ошибка: роль не найдена.", ephemeral=True)

    button.callback = button_callback
    view = discord.ui.View()
    view.add_item(button)
    await ctx.send(embed=embed, view=view)

@bot.event
async def on_ready():
    print("Бот готов к работе!")

bot.run(os.environ['TOKEN'])
