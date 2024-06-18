import discord
from discord.ext import commands

import SteamStore

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents, help_command=None)


@bot.event
async def on_ready():
  print('[Bot] Connected to discord')
  await bot.change_presence(activity=discord.Activity(
      type=discord.ActivityType.watching, name=">StorePrice"))


@bot.command()
async def StorePrice(ctx):
  try:
    content = ctx.message.content.split(' ')[1]
    appid = SteamStore.get_appid(content)
    game_link = SteamStore.get_price(appid)
    link, name, price = game_link

    if price != "Free to Play":
      price = f"{price}"

    embed = discord.Embed(title=f"{name} -> {price}",
                          url=link,
                          colour=0x00b0f4)

    embed.set_author(name="SteamStoreLink")

    embed.set_image(
        url=
        "https://steamcdn-a.akamaihd.net/steamcommunity/public/images/steamworks_docs/english/Header_1.jpg"
    )

    embed.set_thumbnail(url="")

    embed.set_footer(
        text=
        "SteamStoreLink is a projected managed by Brad (_.ze.us._) and is not affiliated with Steam in any way, shape or form."
    )

    await ctx.send(embed=embed)

  except Exception as error:
    await ctx.send(f"[Bot] A error has occured: {error}")


bot.run('')
