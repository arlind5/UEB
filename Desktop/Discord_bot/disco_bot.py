import discord
import os
from dotenv import load_dotenv
load_dotenv()

from discord.ext import commands


TOKEN = os.getenv("Discord_Token")
print(TOKEN)

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '!' , intents = intents)
@client.event

async def on_ready():
    print("The bot is now ready for use!")
    print("-----------------------------")


@client.command()

async def hello(ctx):
    await ctx.send("Hello, Iam Arlind's Bot")

@client.command()
async def add(ctx,left: int,right:int):
    await ctx.send(left + right)

@client.command()
async def whois(ctx, member):
    if member.lower() == "adea":

        await ctx.send("adea is a  billionaire")
    else:
        await ctx.send(f"{member} is fucking millionaire")


@client.command()
async def repeat_this(ctx, content: str , times: int):
    for i in range(times):
        await ctx.send(content + "\n")

@client.command()

async def helpp(ctx):
    await ctx.send("!hello" + "\n" + "!add [num] [num]" + "\n" + "!whois [member]\n" + "!repeat_this [content] [times]\n" )

@client.command()

async def joined(ctx,member: discord.Member):
    if member.joined_at is None:
        await ctx.send(f"{member} has no join date")
    else:
        await ctx.send(f"{member} joined {discord.utils.format_dt(member.joined_at)}")


client.run(TOKEN)