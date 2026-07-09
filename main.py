import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

# Устанавливаем префикс "!" и полностью отключаем встроенную команду !help
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Бот {bot.user} успешно запущен и готов настраивать верификацию!')

# === КОМАНДА !setup ===
@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    # Удаляем сообщение команды, чтобы не засорять чат
    try:
        await ctx.message.delete()
    except:
        pass

    # Создаем красивый эмбед для верификации
    embed = discord.Embed(
        title="🛡️ WERTIX | SECURITY PROTOCOL",
        description="Добро пожаловать в безопасную зону **WERTIX**. Чтобы получить доступ к серверу, вам необходимо подтвердить, что вы являетесь реальным пользователем.",
        color=0x000000
    )
    
    embed.add_field(
        name="📜 РЕГЛАМЕНТ И ПРАВИЛА",
        value="Нажимая кнопку ниже, вы автоматически подтверждаете, что полностью ознакомлены и согласны с правилами сообщества.",
        inline=False
    )
    
    embed.set_footer(text="⚙️ WERTIX SEC | Система автоматической авторизации")

    # Создаем кнопку
    button = discord.ui.Button(
        label="ПРОЙТИ ВЕРИФИКАЦИЮ 🔒",
        style=discord.ButtonStyle.secondary,
        custom_id="verify_button"
    )

    # Логика нажатия на кнопку
    async def button_callback(interaction: discord.Interaction):
        try:
            # Получаем роли по ID
            v_role = interaction.guild.get_role(1523339212517019729)
            u_role = interaction.guild.get_role(1523796444312637621)

            if not v_role or not u_role:
                await interaction.response.send_message("❌ **Ошибка:** Одна из ролей верификации не найдена.", ephemeral=True)
                return

            # Выдаем роль верифицированного и снимаем роль неразрешенного
            await interaction.user.add_roles(v_role)
            await interaction.user.remove_roles(u_role)
            await interaction.response.send_message("✅ **Успешно!** Идентификация пройдена. Приятного общения!", ephemeral=True)

        except Exception as e:
            await interaction.response.send_message(f"⚠️ **Внутренняя ошибка:** Бот не может выдать роль. Проверьте иерархию ролей.", ephemeral=True)

    button.callback = button_callback
    view = discord.ui.View(timeout=None)
    view.add_item(button)

    # Отправляем готовую панель
    await ctx.send(embed=embed, view=view)

# Хэндлер ошибок (чтобы бот просто молчал, если команду пишет не админ)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        return

bot.run(os.environ['TOKEN'])
