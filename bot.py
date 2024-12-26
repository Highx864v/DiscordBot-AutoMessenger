import nextcord
from nextcord.ext import commands, tasks
import asyncio
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ BOT_TOKEN not found in environment variables")

intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    """Event triggered when the bot is ready."""
    print(f"✅ Bot is online! Logged in as {bot.user}")
    auto_send_message.start()

async def send_embed_message(channel):
    """Send an embed message to the specified channel."""
    embed_main = nextcord.Embed(
        title="**Program Status**",
        description=(
            "- example   [Status : `Online`] \n"
            "- example      [Status : `Offline`] \n"
        ),
        color=0x2ecc71  # Green
    )
    embed_shop = nextcord.Embed(
        title="🛒 Buy here: https://localhost/",
        color=0x2ecc71
    )
    embed_shop.set_image(url="https://img2.pic.in.th/pic/360_F_92535664_IvFsQeHjBzfE6sD4VHdO8u5OHUSc6yHF.jpg")
    embed_main.set_footer(text="© Powered By : 864-SHOP")

    await channel.send(
        content="**🎉 New Year Sale: 20% off on all items!** @everyone",
        embeds=[embed_main, embed_shop]
    )

@tasks.loop(seconds=60)
async def auto_send_message():
    """Automated task to send messages at specific times."""
    now_utc = datetime.utcnow()
    now_th = now_utc + timedelta(hours=7)
    current_time = now_th.strftime("%H:%M")
    target_times = ["06:00", "12:00", "18:00"]

    if current_time in target_times:
        channel_id = 1192730488033521734  # Replace with your channel ID
        channel = bot.get_channel(channel_id)
        if channel:
            try:
                await send_embed_message(channel)
                print(f"📤 Message sent to {channel.name}")
            except Exception as e:
                print(f"❌ Failed to send message: {e}")
        await asyncio.sleep(60)

@bot.slash_command(name="send_message", description="Manually send a message to the configured channel.")
async def send_message(interaction: nextcord.Interaction):
    if interaction.user.guild_permissions.administrator:
        channel_id = 1192730488033521734  # Replace with your channel ID
        channel = bot.get_channel(channel_id)
        if channel:
            await send_embed_message(channel)
            await interaction.response.send_message(
                f"📤 Message successfully sent to {channel.name}!", ephemeral=True
            )
    else:
        await interaction.response.send_message(
            "⛔ You lack administrator permissions to use this command.", ephemeral=True
        )

@bot.slash_command(name="restart", description="Restart the bot (Admin only).")
async def restart(interaction: nextcord.Interaction):
    if interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("♻️ Restarting bot...", ephemeral=True)
        print("♻️ Restarting bot...")
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        await interaction.response.send_message(
            "⛔ You lack administrator permissions to use this command.", ephemeral=True
        )

# Start the bot
bot.run(TOKEN)