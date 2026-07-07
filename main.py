import discord
import os
from discord.ext import commands



# 1. Настройка бота
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 2. Логика кнопки
class VerificationView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="ВЕРИФИКАЦИЯ", style=discord.ButtonStyle.primary, custom_id="verify_button_1")
    async def verify(self, interaction: discord.Interaction, button: discord.ui.Button):
        # ЗАМЕНИ ЭТИ ЦИФРЫ НА ID СВОИХ РОЛЕЙ
        role_verified_id = 1523339212517019729 
        role_unverified_id = 1523796444312637621
        
        guild = interaction.guild
        member = interaction.user
        
        v_role = guild.get_role(role_verified_id)
        u_role = guild.get_role(role_unverified_id)
        
        await member.add_roles(v_role)
        await member.remove_roles(u_role)
        
        await interaction.response.send_message("Доступ открыт.", ephemeral=True)

# 3. Команда для создания кнопки
@bot.command()
async def setup(ctx):
    await ctx.send("Нажми кнопку, чтобы получить роль:", view=VerificationView())

@bot.event
async def on_ready():
    bot.add_view(VerificationView())
    print("Бот готов к работе!")

# 4. СЮДА ВСТАВЬ СВОЙ ТОКЕН
bot.run(os.environ["TOKEN"])
