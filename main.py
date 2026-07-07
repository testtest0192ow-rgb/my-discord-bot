@bot.command()
async def setup(ctx):
    if not ctx.author.guild_permissions.administrator:
        return

    # Профессиональный Embed
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
    
    button = discord.ui.Button(label="ПРОЙТИ ВЕРИФИКАЦИЮ", style=discord.ButtonStyle.primary, emoji="🛡️")

    async def button_callback(interaction: discord.Interaction):
        VERIFIED_ROLE_ID = 1523339212517019729
        UNVERIFIED_ROLE_ID = 1523796444312637621
        
        guild = interaction.guild
        v_role = guild.get_role(VERIFIED_ROLE_ID)
        u_role = guild.get_role(UNVERIFIED_ROLE_ID)
        
        try:
            await interaction.user.add_roles(v_role)
            await interaction.user.remove_roles(u_role)
            await interaction.response.send_message("✅ Доступ предоставлен.", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"❌ Ошибка: {e}", ephemeral=True)

    button.callback = button_callback
    view = discord.ui.View(timeout=None)
    view.add_item(button)
    await ctx.send(embed=embed, view=view)
    
