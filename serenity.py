import discord
from discord.ext import commands
import os
startup_extensions = ["belts", "armors"]
from discord.ext.commands import Bot
prefix = ["wiki.", "item."]
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="Serenity and Peace"))
    print("Bot online")
bot.remove_command("help") 
@bot.command()
async def supportserver():
    await bot.say("```Official Support Server``` " + " https://discord.gg/YAZNjbe")
#https://discordapp.com/oauth2/authorize?client_id=430003755405279242&scope=bot

    
@bot.command()
async def invite():
    await bot.say("Invite me with this link: Error...")
@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))
        

@bot.event
async def on_member_join(member):
    server = member.server.default_channel
    fmt = 'Hey! {0.mention} Welcome to {1.name} a place of peace and freedom! Check out #simple_rules and #color_name_request. Enjoy :slight_smile:'
    channel = member.server.get_channel("437518912465403914")
    await bot.send_message(channel, fmt.format(member, member.server))

 
 

    
token = os.environ.get("serenity")
bot.run(f'{token}')
