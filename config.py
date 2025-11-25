# Bot Configuration
# REPLACE THIS WITH YOUR ACTUAL BOT TOKEN
# Get it from: https://discord.com/developers/applications
BOT_TOKEN = "YOUR_BOT_TOKEN"

# Spam Messages (Multiple messages to be randomly selected)
SPAM_MESSAGES = [
    "@everyone SERVER DESTROYED 🔥",
    "@everyone GET FUCKED 💀", 
    "@everyone TERMINATED 🚨",
    "@everyone SAY GOODBYE 👋",
    "@everyone REST IN PEACE ⚰️",
]

# Channel Names (Max 4 types, will be distributed evenly)
CHANNEL_NAMES = [
    "💀⃠ 𝗴𝗲𝘁-𝗻𝘂𝗸𝗲𝗱 ⃠💀",
    "☠️⃠ 𝗴𝗲𝘁-𝗿𝗲𝗸𝘁 ⃠☠️", 
    "🔥⃠ 𝗴𝗲𝘁-𝗳𝗿𝗸𝗲𝗱 ⃠🔥",
    "⚡⃠ 𝗴𝗲𝘁-𝗼𝘄𝗻𝗲𝗱 ⃠⚡"
]

# Number of channels to create (MAX: 500 for Discord limit)
CHANNEL_COUNT = 25  # High but safe from rate limits

# New Server Name After Nuke
NEW_SERVER_NAME = "💀ShadowNuker💀"

# Spam Speed Configuration (in seconds) - MAXIMUM SPEED
SPAM_DELAY_MIN = 0.05  # Ultra fast - 20 messages per second per channel
SPAM_DELAY_MAX = 0.1   # Maximum speed without immediate rate limits