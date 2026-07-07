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
        title="✨ ВЕРИФИКАЦИЯ WERTIX", 
        description="Нажми кнопку ниже, чтобы получить доступ.",
        color=0x2b2d31
    )
    
    button = discord.ui.Button(label="ПРОЙТИ ВЕРИФИКАЦИЮ", style=discord.ButtonStyle.primary, emoji="🛡️")

    async def button_callback(interaction: discord.Interaction):
        # Вставь сюда ID ролей
        v_role_id = 1523339212517019729
        u_role_id = 1523796444312637621
        
        guild = interaction.guild
        v_role = guild.get_role(v_role_id)
        u_role = guild.get_role(u_role_id)
        
        try:
            if v_role: await interaction.user.add_roles(v_role)
            if u_role: await interaction.user.remove_roles(u_role)
            await interaction.response.send_message("✅ Готово!", ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message("❌ Ошибка: У меня нет прав менять роли (подними мою роль выше в настройках сервера!)", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Ошибка: {str(e)}", ephemeral=True)

    button.callback = button_callback
    view = discord.ui.View()
    view.add_item(button)
    await ctx.send(embed=embed, view=view)

bot.run(os.environ['TOKEN'])
