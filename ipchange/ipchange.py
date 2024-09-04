@bot.command(name="changeip")
async def change_ip(ctx):
    try:
        # Execute the commands
        subprocess.run("ipconfig /flushdns", check=True, shell=True)
        subprocess.run("ipconfig /release", check=True, shell=True)
        subprocess.run("ipconfig /renew", check=True, shell=True)
        
        # Send confirmation message
        await ctx.send("✅ IP configuration has been refreshed successfully.")
    except subprocess.CalledProcessError as e:
        # Handle errors during command execution
        await ctx.send(f"⚠️ An error occurred while executing commands: {e}")