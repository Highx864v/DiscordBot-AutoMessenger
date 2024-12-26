# DiscordBot-AutoMessenger

## Overview
DiscordBot-AutoMessenger is a Python-based Discord bot designed to simplify automated messaging, embed creation, and server management. With built-in scheduling and manual message functionality, this bot is perfect for communities that need consistent, professional-grade announcements.

---

## Features
- **Automated Messages:** Schedule messages to be sent at specific times (configured for UTC+7).
- **Custom Embed Messages:** Create rich embeds with titles, descriptions, colors, images, and more.
- **Manual Message Command:** Admins can manually send announcements using a slash command.
- **Bot Restart Command:** Admins can restart the bot directly through Discord.
- **Role-Based Permissions:** Ensures only authorized users (e.g., Administrators) can execute critical commands.

---

## Technologies Used
- **Python**
- **Nextcord** (Discord API wrapper)
- **Asyncio**
- **dotenv** (Environment variable management)

---

## How to Install and Run

### Prerequisites
1. Python 3.8 or higher installed on your system.
2. A Discord account and a bot token (created through the [Discord Developer Portal](https://discord.com/developers/applications)).
3. Install the required dependencies using `pip`.

### Installation Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/DiscordBot-AutoMessenger.git
   cd DiscordBot-AutoMessenger
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Create a .env file in the project directory:
   ```bash
   BOT_TOKEN=your_discord_bot_token_here
4. Run the bot:
   ```bash
    python bot.py

---

## Usage

### Automated Messaging
- **The bot sends automated messages at specific times (06:00, 12:00, 18:00). These times can be adjusted in the code under the target_times list.
### Manual Messaging
- **Use the /send_message slash command to manually send announcements. This requires Administrator permissions.
### Restart Bot
- **Admins can restart the bot with /restart for quick troubleshooting or updates.
