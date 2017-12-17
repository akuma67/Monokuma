#Monokuma by akuma67 and JakeMakesStuff, have fun
#I also made this bot Open Source because why not
#Some code is taken from Dimoniwer and Da532 with permission, thanks guys!

import discord, chalk
import random
from discord.ext import commands
from discord.ext.commands import Bot
from pymongo import MongoClient
import asyncio
import os

bot = commands.Bot(command_prefix="k!")
client = discord.ext.commands.Bot(None)
mclient = MongoClient()

db = mclient.monokuma
strikes = db.strikes

def is_server_staff(ctx):
    x = ctx.message.author.roles
    y = False
    for role in x:
        if role.name == "Staff":
            y = True
    return y

@bot.event
async def on_ready():
    print ("Systems online, Monokuma ready for combat!")
    print ("Current bot user = " + bot.user.name)
    print ("Current bot ID = " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='k!help', type=2), status=discord.Status('online')) #you could set the playing status to anything you want

@bot.command(pass_context=True)
async def thatpersonis(ctx, user: discord.Member):
    embed = discord.Embed(title="can I tell you something?", colour=discord.Colour(0x629aa0), description="You are a complete fucking")

    embed.set_image(url="https://i.imgur.com/aemXiLr.png")
    embed.set_thumbnail(url="https://i.imgur.com/iMt6SGg.png")
    embed.set_author(name="Yo, dude")
    embed.set_footer(text="FUCK OFF", icon_url="https://cdn.discordapp.com/attachments/383375922549751808/383378140921200640/flat800x800070f.jpg")

    embed.add_field(name="piece of shit, and you should rot in hell.", value="Yes, you {}, I'm talking about you!".format(user.name), inline=True)
    embed.add_field(name="You should actually fucking rot in hell.", value="Oh, and just because I was so nice to you in this message, here's a picture of me backstabbing you in TF2.", inline=True)

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("Someone used the ping command.")

@bot.command(pass_context=True)
async def amireally(ctx):
    await bot.say("https://i.imgur.com/jF9hFiQ.png")
    await bot.ban(ctx.message.author)

@bot.command(pass_context=True)
@commands.check(is_server_staff)
async def kick(ctx, user: discord.Member):
    embed = discord.Embed(
        title="User Kicked!",
        colour=discord.Colour(0xB70000),
        description="I have kicked {}!".format(user.name))
    embed.set_thumbnail(
        url=
        "http://fc03.deviantart.net/fs71/f/2014/331/a/3/thumbnail0_by_alandylan12-d87u6yj.png"
    )
    embed.set_author(
        name="Staff Commands",
        icon_url=
        "https://i.imgur.com/ZpCcwYr.png"
    )
    embed.set_footer(
        text="i kicked someone mom!",
        icon_url=
        "https://i.imgur.com/ZpCcwYr.png"
    )
    embed.add_field(
        name="The user you kicked can join at a later date.",
        value="Or, you know you could ban them, just to be sure.",
        inline=True)
    await bot.say(embed=embed)
    await bot.kick(user)


@bot.command(pass_context=True)
@commands.check(is_server_staff)
async def ban(ctx, user: discord.Member):
    embed = discord.Embed(
        title="{} has been banned!".format(user.name),
        colour=discord.Colour(0xE50000),
        description="You can revoke the ban at a later date.")

    embed.set_thumbnail(url="https://www.flamingtoast.com/wp-content/uploads/2015/04/ban-hammer-newB-1000x1000.jpg")
    embed.set_author(name="Staff Commands", icon_url="https://i.imgur.com/ZpCcwYr.pngg")
    embed.set_footer(text="i banned someone mom!", icon_url="https://i.imgur.com/ZpCcwYr.png")

    await bot.say(embed=embed)
    await bot.ban(user)

@bot.command(pass_context=True)
@commands.check(is_server_staff)
async def strike(ctx, user: discord.Member, *, reason):
    strikes.insert_one({"staff_id" : ctx.message.author.id, "user_id" : user.id, "reason" : reason})

    embed = discord.Embed(
        title="{} has been striked!".format(user.name), 
        colour=discord.Colour(0x573dcd))

    embed.set_thumbnail(url="https://i.imgur.com/u6rgacC.png")
    embed.set_author(name="Staff Commands", url="https://discordapp.com", 
    icon_url="https://i.imgur.com/ZpCcwYr.png")
    embed.set_footer(text="i striked someone mom!", 
    icon_url="https://i.imgur.com/ZpCcwYr.png")

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def about(ctx):
    embed = discord.Embed(
        title="Monokuma is",
        colour=discord.Colour(0x323298),
        description="made by **akuma67#6339** and **Jake#0009**")

    embed.set_thumbnail(url="https://i.imgur.com/JCeJrB9.jpg")
    embed.set_author(name="About This Bot", icon_url="https://i.imgur.com/ZpCcwYr.png")
    embed.set_footer(text="MonokumaPY, made with ❤️", icon_url="https://i.imgur.com/ZpCcwYr.png")

    embed.add_field(name="What is this bot and what does it do? 🤔", value="This bot can do many things, such as show memes, chat with you, and many more! It can also do some serious things, such as moderation commands.  The full command list can be viewed if you use the command **help.** ")
    embed.add_field(name="Oh fuck, something broke!  What do I do?", value="It's alright! Just contact me about any issues, and I'll fix them. ")
    embed.add_field(name="Make Monokuma your own!", value="Monokuma's full source code is available at https://github.com/akuma67/Monokuma.", inline=True)

    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def creator(ctx):
    embed = discord.Embed(title="I'd like to show you the creator of this bot!",
    colour=discord.Colour(0x2da6ee),
    description="With beautiful ~~fringe~~ eyes, and beautiful ~~fringe~~ lips, and a beautiful ~~fringe~~ chin.")

    embed.set_image(url="https://i.imgur.com/PNOgnSP.jpg")
    embed.set_thumbnail(url="https://i.imgur.com/r33Xw2C.png")
    embed.set_author(name="Hello")
    embed.set_footer(text="mr. worldwide", icon_url="https://i.imgur.com/ZpCcwYr.png")

    embed.add_field(name="How could you not fall for him?", value="Oh look, here he is now!", inline=True)

    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def profile(ctx, user: discord.Member):
    embed = discord.Embed(colour=discord.Colour(0xd04105))

    embed.set_thumbnail(url=user.avatar_url)
    embed.set_author(name="Profile of {}".format(user.name))
    embed.set_footer(text="Monokuma", icon_url="https://i.imgur.com/ZpCcwYr.png")

    embed.add_field(name="Username", value="{}".format(user.name))
    embed.add_field(name="User ID", value="{}".format(user.id))
    embed.add_field(name="Status", value="{}".format(user.status))
    embed.add_field(name="Role", value="{}".format(user.top_role))
    embed.add_field(name="Join date", value="{}".format(user.joined_at))

    await bot.say(embed=embed)

bot.run("token") #enter your token here if you're making a new instance
