@bot.command(name="purge")
@commands.has_guild_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    if amount < 1 or amount > 100:
        await ctx.send("Amount must be between 1 and 100.")
        return

    def check_DELETE(discord.Message):
        return isinstance(discord.Message, discord.Message) and not discord.Message.pinned and discord.Message.type != discord.MessageType.default

    await ctx.channel.purge(messages=amount, check=check_delete)
    await ctx.send(f"Purged {amount} messages.")