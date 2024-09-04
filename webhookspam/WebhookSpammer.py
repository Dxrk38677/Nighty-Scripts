@bot.command(name="spamwebhook")
async def spamwebhook(ctx, webhook: str, message: str, amount: int=10, avatar_url: str="https://images-ext-1.discordapp.net/external/Md6Blc8OOesM-D1Y8RDGCWWyQorb3MpcylxR5w8F7IU/https/i.pinimg.com/564x/88/e8/e9/88e8e969ff0e416599ea4140e88d59f3.jpg?format=webp", delay: float=0.5):
    await ctx.message.delete()
    for x in range(amount):
        requests.post(webhook, json={"content": message, "avatar_url": avatar_url})
        await asyncio.sleep(delay)
