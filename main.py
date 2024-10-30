import discord
from discord.ext import commands
import asyncio
import random
import B
import os

from discord import Client
from discord import Intents

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!!', intents=intents)

@client.event
async def on_ready():
    # Wait for the bot to be fully ready
    await client.wait_until_ready()
    print("Logged in as {}".format(client.user.name))
    await client.change_presence(activity=discord.Game("VERIFICATION"))


@client.event
async def on_message(message):
    if message.author.id == 772847742484873237 :
        return

    if message.content.upper().startswith('VERIFY'):
        answer = random.randint(1000, 9999)
        embed = discord.Embed(color=0x00ff00)
        embed.title = "VERIFICATION" 
        embed.description = '**Code:** {}\n\n{}\nRE ENTER THE VERIFICATION CODE HERE OR IN THE CHANNEL \n\n CODE GENEREATED FROM CHANNEL <#{}>\nFROM SERVER `{}`'.format(answer, message.author.mention, message.channel.id, message.author.guild.name)
        channel = await message.author.create_dm()
        await channel.send(embed=embed)
        await message.channel.send("{} you got your code in dm ".format(message.author.mention))

        def is_correct(m):
            return m.author == message.author and m.content.isdigit()

        try:
            guess = await client.wait_for('message', check=is_correct, timeout=120.0)
        except asyncio.TimeoutError:
            embed = discord.Embed(color=0x00ff00)
            embed.title = "VERIFICATION" 
            embed.description = '{} \nYOU TOOK TO LONG TO RESPONSE'.format(message.author.mention)
            await channel.send(embed=embed)
            embed.description = '{} \nVERIFICATION CANCLED'.format(message.author.mention)
            await message.channel.send(embed=embed)
            return

        if int(guess.content) == answer:
            role = discord.utils.get(message.guild.roles, name='verified')
            if role is not None:
                await message.author.add_roles(role)
                embed = discord.Embed(color=0x00ff00)
                embed.title = ":white_check_mark: SUCCESSFULL" 
                embed.description =  "{} CONGO  YOU ARE VERIFIED SUCCESSFULLY!".format(message.author.mention)
                await channel.send(embed=embed)
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(color=0xff0000)
                embed.title = ":warning: ERROR!!" 
                embed.description = "{}  The 'verified' role was not found on the server.".format(message.author.mention)
                await channel.send(embed=embed)
                await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(color=0xff0000)
            embed.title = ":warning: ERROR!!" 
            embed.description = "{} WRONG CODE THE CODE WAS  `{}`.\nTYPE VERIFY IN <#{}> CHANNELTO GET YOUR VERIFICATION CODE AGAIN".format(message.author.mention, answer, message.channel.id)
            await channel.send(embed=embed)
            await message.channel.send(embed=embed)

@client.command()
async def setup(ctx):
    await ctx.send("working")

B.b()
#client = MyClient(intents=intents)
my_secret = os.environ['TOKEN']
client.run(my_secret)

