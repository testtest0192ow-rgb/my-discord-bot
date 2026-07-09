import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="wertix_verify_hidden_", intents=intents)

@bot.command()
async def setup(ctx):
    # Удаляем сообщение команды, чтобы не было лишнего мусора
    try:
        await ctx.message.delete()
    except:
        pass

    embed = discord.Embed(
        title="🛡️ WERTIX | SECURITY PROTOCOL",
        description=" Добро пожаловать в безопасную зону **WERTIX**. Чтобы получить полный доступ к текстовым и голосовым каналам, вам необходимо подтвердить свой аккаунт.",
        color=0x000000
    )
    
    embed.add_field(
        name="📜 РЕГЛАМЕНТ И ПРАВИЛА",
        value="Нажимая кнопку ниже, вы автоматически подтверждаете, что ознакомлены с правилами нашего сообщества и обязуетесь их соблюдать.",
        inline=False
    )
    
    embed.set_footer(text="⚙️ WERTIX SEC | Система автоматической авторизации")

    # Создаем кнопку верификации со смайликом
    button = discord.ui.Button(
        label="ПРОЙТИ ВЕРИФИКАЦИЮ  🔓", 
        style=discord.ButtonStyle.secondary,
        custom_id="verify_button"
    )

    async def button_callback(interaction: discord.Interaction):
        try:
            # Получаем роли по ID
            v_role = interaction.guild.get_role(1523339212517019729)
            u_role = interaction.guild.get_role(1523796444312637621)

            if not v_role or not u_role:
                await interaction.response.send_message("❌ **Ошибка:** Необходимые роли не найдены в системе. Свяжитесь с администрацией.", ephemeral=True)
                return

            await interaction.user.add_roles(v_role)
            await interaction.user.remove_roles(u_role)
            await interaction.response.send_message("✅ **Успешно!** Идентификация пройдена. Все каналы сервера теперь открыты для вас. Приятного общения!", ephemeral=True)
            
        except Exception as e:
            # Если бот не может выдать роль (например, нет прав)
            await interaction.response.send_message(f"⚠️ **Внутренний сбой системы:** {e}", ephemeral=True)

    button.callback = button_callback
    view = discord.ui.View(timeout=None)
    view.add_item(button)
    
    await ctx.send(embed=embed, view=view)

bot.run(os.environ['TOKEN'])
