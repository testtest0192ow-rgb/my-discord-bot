import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command()
async def setup(ctx):
    # Удаляем сообщение команды, чтобы не было лишнего мусора
    try:
        await ctx.message.delete()
    except:
        pass

    embed = discord.Embed(
        title="◈ WERTIX | SECURITY PROTOCOL",
        description="Добро пожаловать на WERTIX. Для получения полного доступа к ресурсам сервера и открытия каналов связи необходимо пройти процедуру верификации.",
        color=0x000000
    )
    embed.add_field(
        name="РЕГЛАМЕНТ", 
        value="Нажатие кнопки ниже подтверждает ваше согласие с внутренними правилами сообщества и готовность следовать установленным стандартам общения.", 
        inline=False
    )
    embed.set_footer(text="WERTIX © 2026 | Идентификация пользователя")
    
    # Кнопка с ID
    button = discord.ui.Button(label="ПРОЙТИ ВЕРИФИКАЦИЮ", style=discord.ButtonStyle.primary, emoji="🛡️")

    async def button_callback(interaction: discord.Interaction):
        try:
            # Получаем роли
            v_role = interaction.guild.get_role(1523339212517019729)
            u_role = interaction.guild.get_role(1523796444312637621)
            
            if not v_role or not u_role:
                await interaction.response.send_message("Ошибка: Роли не найдены на сервере.", ephemeral=True)
                return

            await interaction.user.add_roles(v_role)
            await interaction.user.remove_roles(u_role)
            await interaction.response.send_message("✅ Доступ предоставлен.", ephemeral=True)
        except Exception as e:
            # Если бот не может выдать роль (например, нет прав)
            await interaction.response.send_message(f"❌ Ошибка прав: {e}", ephemeral=True)

    button.callback = button_callback
    view = discord.ui.View(timeout=None)
    view.add_item(button)
    await ctx.send(embed=embed, view=view)

bot.run(os.environ['TOKEN'])
