@bot.command(name="locateip")
async def locate_ip(ctx, ip: str):
    try:
        # Inform the user that the lookup is in progress
        await ctx.send(f"🔍 Looking up information for IP: `{ip}`...")

        # Perform the IP lookup
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        # Check if the API returned a valid response
        if data['status'] == 'success':
            # Construct the response message as a list
            message = (
                f"**IP Lookup Result**\n\n"
                f"**IP Address**: {data['query']}\n"
                f"**Country**: {data['country']}\n"
                f"**Region**: {data['regionName']}\n"
                f"**City**: {data['city']}\n"
                f"**ISP**: {data['isp']}\n"
                f"**Latitude**: {data['lat']}\n"
                f"**Longitude**: {data['lon']}\n"
                f"**Timezone**: {data['timezone']}\n"
                f"**Organization**: {data.get('org', 'N/A')}\n"
                f"**Google Maps**: [Open Location](https://www.google.com/maps?q={data['lat']},{data['lon']})"
            )
            
            # Send the message to the channel
            await ctx.send(message)
        else:
            # Handle the case when IP data is not found
            await ctx.send(f"❌ Could not find information for IP: `{ip}`. Please check the IP address and try again.")
    
    except requests.RequestException as e:
        # Handle exceptions that may occur during the request
        await ctx.send(f"⚠️ An error occurred while fetching data: {e}")

    except Exception as e:
        # Handle any other exceptions
        await ctx.send(f"⚠️ An unexpected error occurred: {e}")