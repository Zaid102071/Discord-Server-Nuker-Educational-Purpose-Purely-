# 🔥 Shadow Nuker - Ultimate Discord Server Management Tool
<img width="1366" height="768" alt="Screenshot (2)" src="https://github.com/user-attachments/assets/c5ab3cd7-82b0-49b1-89aa-7000624bc10e" />
<img width="1366" height="768" alt="Screenshot (13)" src="https://github.com/user-attachments/assets/7a3a97f6-600e-4644-b363-516578d0a21a" />
<img width="1366" height="768" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/093919cb-f970-4b96-8c03-f16421cb7aaa" />


> **⚠️ WARNING: FOR EDUCATIONAL PURPOSES ONLY**  
> This tool is designed for educational and authorized server testing only. Misuse of this software may violate Discord's Terms of Service and result in account termination.

![Shadow Nuker Banner](https://via.placeholder.com/800/200/000000/FFFFFF?text=SHADOW+NUKER)

## 👨‍💻 Developed by Z61D
**Creator & Maintainer**: Zaid The Dev  
**GitHub**: [https://github.com/Z61D](https://github.com/Zaid102071)  
**About Me**: https://github.com/Z61D/About-Me-Bio

> *"Powerful tools require responsible usage"* - Z61D

## 🎯 Features

### 💀 Destruction Capabilities
- **Mass Channel Management**: Create/delete hundreds of channels instantly
- **Server Identity Override**: Rename servers with custom names
- **Distributed Spam System**: Intelligent message distribution across multiple channels
- **Customizable Chaos**: Fully configurable destruction parameters
- You Can Set The number of channel to be created
- You Can Customize the messages to Be spammed and channels name server name 
- You Can Cuztomize speed and almost everything not like other nukers that takes credits

### 🎨 Premium Interface
- **Smooth Gradient Effects**: Beautiful purple-to-pink color transitions
- **Professional Console UI**: Clean, organized menu system
- **Real-time Status Updates**: Live progress indicators and statistics
- **Actaully very Fast** More than 1k pings in 30 secs

### ⚙️ Advanced Configuration
- **External Config System**: Edit settings without recompiling
- **Modular Architecture**: Easy to customize and extend
- **Rate Limit Aware**: Intelligent timing to avoid detection
<img width="1366" height="768" alt="Screenshot (2)" src="https://github.com/user-attachments/assets/c5ab3cd7-82b0-49b1-89aa-7000624bc10e" />
<img width="1366" height="768" alt="Screenshot (13)" src="https://github.com/user-attachments/assets/7a3a97f6-600e-4644-b363-516578d0a21a" />
<img width="1366" height="768" alt="Screenshot (12)" src="https://github.com/user-attachments/assets/093919cb-f970-4b96-8c03-f16421cb7aaa" />

## 📖 Manual Usage Guide

### Step 1: Preparation
1. **Create a Discord Bot**:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a New Application
   - Go to "Bot" section and create a bot
   - Copy the bot token

2. **Invite Bot to Server**:
   - In OAuth2 > URL Generator, select "bot" scope
   - Enable Administrator permissions
   - Use the generated link to invite bot to your server

### Step 2: Configuration
Edit `config.py` with your settings:
```python
# Bot Configuration
# REPLACE THIS WITH YOUR ACTUAL BOT TOKEN
# Get it from: https://discord.com/developers/applications
BOT_TOKEN = "You Token Of BOT"

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
