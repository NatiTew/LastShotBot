import discord
from discord.ext import commands
from config import *

bot = commands.Bot(command_prefix=PREFIX, description="AepmongBot")


@bot.event
async def on_ready():
    print("Aepmong")


@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send('hello I am LastShotBot')

# @bot.command(pass_context=True)
# async def clean(ctx, amount: str):
#     if amount == 'all':
#         await ctx.channel.purge()
#     else:
#         await ctx.channel.purge(limit=(int(amount) + 1))

@bot.command(name='clear')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    authors = {}
    async for message in ctx.channel.history(limit=amount + 1):
        if message.author not in authors:
            authors[message.author] = 1
        else:
            authors[message.author] += 1
        await message.delete()

    msg = "\n".join([f"{author}:{amount}" for author,
                     amount in authors.items()])
    await ctx.channel.send(msg)

@bot.command(pass_context=True)
async def bye(ctx):
    await ctx.message.add_reaction('‼️')
    # await ctx.send('hello I am LastShotBot')
    msg = await ctx.send('hello I am LastShotBot')
    await msg.add_reaction('🚴')
    await msg.add_reaction('🏳️')




bot.run(TOKEN, bot=True, reconnect=True)