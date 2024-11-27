import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the Discord bot token from the environment
TOKEN = os.getenv('DISCORD_TOKEN')

# Intents and bot setup
intents = discord.Intents.default()
intents.members = True  # Required for on_member_join event
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is connected and ready!")

@bot.event
async def on_member_join(member):
    # Replace 'welcome' with the name of your welcome channel
    channel = discord.utils.get(member.guild.text_channels, name='স্বাগত')
    if channel:
        # Welcome message with emojis and copyable format
        message = (
            f"🌟 **বাংলার প্রাঙ্গণে আপনাকে স্বাগতম প্রিয়!** {member.mention} 🌟\n\n"
            f"📜 **শুরতেই সার্ভার নির্দেশিকা থেকে সার্ভার এর সব নিয়ম কানুন দেখে নিন।**\n"
            f"🛠️ **এরপর \"ভূমিকা-গ্রহণ\" চ্যানেল থেকে আপনার পজিশন অনুযায়ী রোল গ্রহণ করুন।**\n\n"
            f"👉 **এইবার নিচের ফরম্যাটে লিখুন:**\n"
            f"```\n"
            f"@Server Moderator please give me role of <your position>\n"
            f"```\n"
            f"🚀 **পজিশন হতে পারে:** সাব-প্যানেল / প্যানেল / সিনিয়র প্যানেল / সুপারভাইজর / সিনিয়র সুপারভাইজর\n"
        )
        await channel.send(message)

# Run the bot with the token from the .env file
bot.run(TOKEN)
