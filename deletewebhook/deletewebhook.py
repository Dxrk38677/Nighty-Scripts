@bot.command(name="deletewebhook")
async def delete_webhook(ctx, webhook_url: str):
    try:
        # Attempt to delete the webhook
        webhook = await bot.fetch_webhook(webhook_url.split('/')[-1])
        await webhook.delete()
        await ctx.send(f"Webhook deleted successfully.")
        logger.info(f"Webhook deleted successfully: {webhook_url}")
    except discord.NotFound:
        await ctx.send("Webhook not found.")
        logger.error("Webhook not found.")
    except discord.Forbidden:
        await ctx.send("I do not have permission to delete this webhook.")
        logger.error("Forbidden: I do not have permission to delete this webhook.")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to delete webhook: {e}")
        logger.error(f"HTTPException: Failed to delete webhook: {e}")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        logger.error(f"An unexpected error occurred: {e}")
