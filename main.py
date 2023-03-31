import discord
from discord.ext import commands

intents = discord.Intents.all()

client = commands.Bot(command_prefix = '!', intents = intents)

@client.command(name="delete")
async def delete(ctx):
    await ctx.channel.purge(limit=100)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run("MTA5MTI1OTI5MzMxNzIxODMwNA.GK826G.63dgEjpDU6kMt_oa7xLNnjAgonjJOTXVAFddKo")