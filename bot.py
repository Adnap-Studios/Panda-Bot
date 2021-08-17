import discord
from discord.ext import commands
import aiohttp

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

@bot.event
async def on_member_join(member):
    print(f'{member} joined the server!')

@bot.event
async def on_message(message):
    if '!map' in str(message.content).lower():
        await message.channel.send(get_map_links())
    else:
        await bot.process_commands(message)

@bot.command(aliases=['map'])
async def dynmap(ctx):
    print('Posting map...')
    await ctx.send(get_map_links())

@bot.command(name='setuprules')
async def rules(ctx):
    print('Posting rules...')
    embed = discord.Embed(title="General Rules", description=get_rules(), color=0x00ff00)
    embed.set_thumbnail(url="https://www.panda-smp.com/uploads/logos/160f56ed100afb_jelgikqhmfonp.png")
    embed.set_footer(text="PandaSMP © 2021")
    await ctx.send(embed=embed)

@bot.command()
async def panda(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/panda')
      panda = await request.json()
      request2 = await session.get('https://some-random-api.ml/facts/panda')
      fact = await request2.json()

   embed = discord.Embed(title="Panda!", color=discord.Color.purple())
   embed.set_image(url=panda['link'])
   embed.set_footer(text=fact['fact'])
   await ctx.send(embed=embed)

def get_map_links():
    links = 'PandaSMP Live Maps:\n🌍 EarthSMP: https://earth.panda-smp.com/'
    return links

def get_rules():
    emoji = discord.utils.get(bot.emojis, name='pandasmp')
    rules = f"""
            { emoji } Respect other.
            { emoji } No advertising or mentioning other servers.
            { emoji } Don’t ask to become staff.
            { emoji } Don’t impersonate staff.
            { emoji } No spamming.
            { emoji } No racism.
            { emoji } No all caps talking. This is considered shouting.
            { emoji } No unapproved links.
            { emoji } No begging. Asking nicely once or twice is acceptable.
            { emoji } No griefing. Please do not destroy, deface, graffiti, or build on top of another person’s constructions.
            { emoji } No 1×1 tall towers or holes.
            { emoji } Please don’t try and crash the plugins or bots
            { emoji } No hacking. Using interface mods or programs to circumvent our security system can lead to being banned
            { emoji } No player killing in non-player killing areas.
            { emoji } No massive redstone clocks or devices that run 24/7 without approval.
            { emoji } No offensive builds, names or skins.
            { emoji } No death traps or places where other users will definitely die
            { emoji } No scamming players.
            { emoji } Be appropriate, No counting up or down.
            { emoji } Don’t complain about lag.
            { emoji } Don’t curse in public chats or in personal ones.
            { emoji } In-game chat can be seen in Discord and vice versa, be nice to people!
            """
    return rules

bot.run('ODY0NzYwODM0MzI0NjkzMDAy.YO6JSQ.1G_ZC6KUzwvRiPrO4RD8FglvOOQ')
