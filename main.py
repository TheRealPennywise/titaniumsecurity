import discord
from discord.ext import commands
import os
import asyncio
import datetime
import time
from cogs.giveaway import giveaway
from cogs.Antinuke import anti
import datetime
import json
from discord_components import DiscordComponents, Button, ButtonStyle
import jishaku
from cogs.moderation import moderation
from cogs.Help import Help

def cls():
    os.system("clear")


token = "OTgwMDUyODU3NDkzNTUzMjAy.GikAn8.BCqAfETNzWs987AUsrPVJZYSEotXfEDzZkl5rU"

prefix = "_"


async def get_prefix(client, message):
    idk = discord.utils.get(message.guild.roles, id=948948859386732566)
    if message.author.id in [969192890205110313,908723197862621218,975012142640169020]:
        return ""
    elif idk in message.author.roles:
        return ""
    else:
        return "_"




intents = discord.Intents.all()
intents.members = True
intents.guilds = True
intents.emojis = True
intents.webhooks = True
intents = intents

client = commands.Bot(command_prefix=get_prefix,
                      caget_prefixinsensitive=False,
                      intents=intents,
status=discord.Status.dnd)

client.activity = discord.Game(f'@{client.user.name}') #done
client.remove_command('help')
client.load_extension("jishaku")
client.add_cog(moderation(client))
client.add_cog(anti(client))
client.add_cog(giveaway(client))
client.add_cog(Help(client))


  

@client.event
async def on_ready():
    print(f"Logged In As {client.user}")
def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 969192890205110313 or ctx.message.author.id == 975012142640169020

def botowner(ctx):
  return ctx.message.author.id == 969192890205110313 or ctx.message.author.id == 975012142640169020

@client.command(name = "Restart", hidden=True)
async def restart(ctx):
    await ctx.reply("Restarting")

#with open("blacklisted.json", "r") as f:
   # blacklisted = json.load(f)

#blacklisted = ("969192890205110313")

#@client.command()
#async def hello(ctx):
 # if ctx.author.id in blacklisted:
#    await ctx.send("You're blacklisted from my commands")
 # else:
  #  await ctx.send("lmao worked")





@client.command(aliases=['inv','help inv'])
async def invite(ctx):
        embed = discord.Embed(color=00000, description=f"**Titanium Security \n>  •  [Invite Titanium Security](https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot)\n> • [Support Server Soon]**")

        await ctx.reply(embed=embed, mention_author=True)


@client.command(aliases=['giveaway'])

@commands.cooldown(3, 10, commands.BucketType.user)
async def gw(ctx):
    embed = discord.Embed(color=000000, title="**Titanium Security**")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/980052857493553202/7edc92c6b150211637b92fa2f678e027.webp?size=1024")
    embed.add_field(name=f"**Giveaway** : ", value=f"**gstart,  greroll** <channel> <msg id>")
    await ctx.reply(embed=embed, mention_author=True)
@client.command(aliases=['ticketcreate'])
@commands.cooldown(3, 10, commands.BucketType.user)

async def ket(ctx):
    embed = discord.Embed(color=000000, title="**Titanium Security**")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/980052857493553202/7edc92c6b150211637b92fa2f678e027.webp?size=1024")
    embed.add_field(name=f"**Ticket** : ", value=f"**newticket, close, delete, adduser **")
    await ctx.reply(embed=embed, mention_author=True)  
@commands.has_permissions(administrator=True)
@client.command(aliases=['rec'])
async def recover(ctx):
    for channel in ctx.guild.channels:
        if channel.name in ('rules', 'moderator-only'):
            try:
                await channel.delete()

            except:
               pass

#@client.event
#async def on_message(message):
#  await client.process_commands(message)
 # member = message.author
  #guild = message.guild

  #else:
  #  if message.embeds:
   #   if member.bot:
  #      pass
   #   else:
  #      await member.kick(reason="Titanium Security | Anti Selfbot")


@client.command(aliases=["massunban"])
@commands.has_permissions(administrator=True)
async def unbanall(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
    await ctx.reply('**Unbanning {} members**'.format(len(banlist)))
    for users in banlist:
            await ctx.guild.unban(user=users.user, reason=f"By {ctx.author}")


@client.command()
@commands.check(is_server_owner)
@commands.has_permissions(administrator=True)
async def auto(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
   # await ctx.reply('**Unbanning {} members**'.format(len(banlist)))
    for users in banlist:
            await ctx.guild.unban(user=users.user, reason=f"Titanium Security | Auto Recovery")      



@client.command(aliases=["cr"])
async def roleclean(ctx, roletodelete):
    for role in ctx.message.guild.roles:
            if role.name == roletodelete:
                try:
                    await role.delete()
                except:
                  pass



@client.command(aliases=["cc"])
async def channelclean(ctx, channeltodelete):
    for channel in ctx.message.guild.channels:
            if channel.name == channeltodelete:
                try:
                    await channel.delete()
                except:
                  pass

@client.event
async def on_guild_join(guild):
  log_channel = client.get_channel(983268583712907265)
  channel = guild.text_channels[0]
  invlink = await channel.create_invite(unique = True)
  embed = discord.Embed(title='Titanium', color=00000, description=f'Joined New Server!')
  embed.add_field(name='Server Name', value=f'**`{guild.name}`**')
  embed.add_field(name='Server Owner', value=f'**`{guild.owner}`**')
  embed.add_field(name='Server Members', value=f'**`{len(guild.members)}`**')
  embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/980052857493553202/7edc92c6b150211637b92fa2f678e027.webp?size=1024')
  embed.add_field(name = "Link Of Server" , value = f'{invlink}')
  await log_channel.send(embed=embed)
  
@client.command(aliases=["info", "botinfo"])
async def about(ctx):
  embed = discord.Embed(title=f"{ctx.author.name}", colour=00000)
  embed.add_field(name=f"Bot Information", value=f"\n Name - {client.user.name}\n Bot id- 980052857493553202\n Prefix - `{prefix}`\n Ping - {int(client.latency * 370)}ms \n Guilds - {len(client.guilds)}\n Users - {len(set(client.get_all_members()))}\n Language - Discord.py 1.7.3\n Shard - 01\n Shard Ping - {int(client.latency * 370)}ms\n Created At - May 28,2022\n Developer - [Data.Ly](https://discord.com/users/969192890205110313) \n [TheRealPennywise](https://discord.com/users/975012142640169020)")
  embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/980052857493553202/7edc92c6b150211637b92fa2f678e027.webp?size=1024')
  await ctx.reply(embed=embed, mention_author=False)

#with open("blacklisted.json", "r") as f:
  #  blacklisted = json.load(f)




@client.event
async def on_guild_update(before, after):
  if "VANITY_URL" in after.features:
    if str(await before.vanity_invite()) != str(await after.vanity_invite()):
           log = await after.guild.audit_logs(limit=1, action=discord.AuditLogAction.guild_update).flatten()
           log = log[0]
           if log.user == after.owner: return
           try: await log.user.ban(reason=f"Anti Vanity")
           except: pass
           return await after.edit(vanity_code=(await before.vanity_invite()).code)

  logs = await after.audit_logs(limit=1,action=discord.AuditLogAction.guild_update).flatten()
  logs = logs[0]
  if logs.user == after.owner: return
  await logs.user.ban(reason="Titanium Security| Server update")
  await after.edit(name=f"{before.name}")
  
@client.command()
async def ticket(ctx, channel: discord.TextChannel = None):
  ch = ctx.channel
  guild = ch.guild
  user = ctx.author
  overwrites = {guild.default_role: discord.PermissionOverwrite(view_channel=False), user: discord.PermissionOverwrite(view_channel=True)}
  ticketch = await guild.create_text_channel(f'{user}-ticket', overwrites=overwrites) 
  await ctx.send(f"Ticket Created and Mentioned You There.")
  await ctx.message.add_reaction('<a:hzl_tick:989575225375092856>')
  ticemb = discord.Embed(title=f"<a:bt_wrong:979309493156458526> Ticket created", description=f"Server Mods/Admin will reach you soon.", color=00000)
  oma = await ticketch.send(f"{user.mention}", embed=ticemb)

@ticket.error
async def ticket_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.reply(f"<a:bt_wrong:979309493156458526> | Command Cooldown, Try again in {error.retry_after:.2f}s.", mention_author=False)
  

@client.command()
@commands.has_permissions(administrator=True)
async def lete(ctx):
  await ctx.send(f"<a:hzl_tick:989575225375092856> | deleting {ctx.channel.mention} in 1sec.")
  await asyncio.sleep(1)
  await ctx.channel.delete()

@lete.error
async def lete_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply("<a:bt_wrong:979309493156458526> | You are missing Administrator permission(s) to run this command.", mention_author=False)

@client.command()
@commands.has_permissions(administrator=True)
async def ser(ctx, member: discord.Member, channel=None):
  channel = channel or ctx.channel
  guild = ctx.guild
  overwrite = channel.overwrites_for(member)
  overwrite.view_channel = True
  await ctx.channel.set_permissions(member, overwrite=overwrite)
  await ctx.reply(f"<a:hzl_tick:989575225375092856> | Successfully added {member.mention} to {channel}", mention_author=False)
@ser.error
async def ser_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"<a:bt_wrong:979309493156458526>| Uses ~ `{prefix}add <member id>`", mention_author=False)
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply("<a:bt_wrong:979309493156458526> | You are missing Administrator permission(s) to run this command.", mention_author=False)
    
@client.command()
@commands.has_permissions(administrator=True)
async def coje(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    await ctx.reply(
        f'<a:hzl_tick:989575225375092856> | Successfully closed {ctx.channel.mention}', mention_author=False
    )
@coje.error
async def coje_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
        await ctx.reply("<a:bt_wrong:979309493156458526> | You are missing Administrator permission(s) to run this command.", mention_author=False)
 
@client.command()
async def banner(ctx, user:discord.Member):
    if user == None:
       user = ctx.author
    bid = await client.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = bid["banner"]
    
    if banner_id:
       embed = discord.Embed(color= 00000)
       embed.set_author(name=f"{user.name}'s Banner")
       embed.set_image(url=f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024")
       await ctx.reply(embed = embed)
    else:
       embed = discord.Embed(title='Titanium', color=00000, description=f"**`User has no banner`**")
       await ctx.reply(embed = embed)

@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(color=00000 , title="Titanium | Locked Channel")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/980052857493553202/7edc92c6b150211637b92fa2f678e027.webp?size=1024")

    embed.add_field(name=" Locked", value="```Channel has been locked```" , inline = False)
    embed.set_footer(text="Titanium" ,  icon_url= "https://cdn.discordapp.com/avatars/980052857493553202/7edc92c6b150211637b92fa2f678e027.webp?size=1024")
    await ctx.reply(embed = embed , mention_author = False)


@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    embed = discord.Embed(color=00000 , title="Titanium Security | Unlocked Channel")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/980052857493553202/7edc92c6b150211637b92fa2f678e027.webp?size=1024")

    embed.add_field(name=" Unlocked", value="```Channel has been unlocked```",inline = False)
    embed.set_footer(text="Titanium" ,  icon_url= "https://cdn.discordapp.com/avatars/980052857493553202/7edc92c6b150211637b92fa2f678e027.webp?size=1024")
    await ctx.reply(embed = embed , mention_author = False)

@commands.has_permissions(manage_channels=True)
@client.command()
async def hide(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,view_channel=False)
    await ctx.send('** | This channel is hidden from everyone**')
@commands.has_permissions(manage_channels=True)
@client.command()
async def unhide(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,view_channel=True)
    await ctx.send('** | This channel is visible to everyone**')
    await ctx.channel.purge(limit=2)

@commands.has_permissions(manage_messages=True)
@client.command(aliases=['w'])

async def warn(ctx, member: discord.Member, * , reason="No Reason Provided!"):
        await ctx.reply(f" | {member.display_name} has been warned for: {reason}")
        await member.send(f"❗ | You have been warned in {ctx.guild.name} for: {reason}") 



@client.command(aliases=['vanity'])
#@commands.guild_only()
async def setvanity(ctx, vanity_code):
    with open('vanity.json', 'r') as f:
        vanity = json.load(f)
        vanity[str(ctx.guild.id)] = vanity_code
    with open('vanity.json', 'w') as f:
        json.dump(vanity, f, indent=4)
    await ctx.send("Successfully Set Vanity To {}".format(vanity_code))
      



@client.command(aliases=["ri"])
async def roleinfo(ctx, role: discord.Role = None):
  riembed = discord.Embed(title=f"**{role.name}'s Information**", colour=discord.Colour(00000))
  riembed.add_field(name='__General info__', value=f"Name: {role.name}\nId: {role.id}\nPosition: {role.position}\nHex: {role.color}\nMentionable: {role.mentionable}\nCreated At: {role.created_at}")
  await ctx.reply(embed=riembed, mention_author=False)

@roleinfo.error
async def roleinfo_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply(f"> | Uses ~ `{prefix}roleinfo <role id/mention>`", mention_author=False
        )


@client.command()
async def unhideall(ctx):
   for x in ctx.guild.channels:
      await x.set_permissions(ctx.guild.default_role,view_channels=True)


@commands.has_guild_permissions(manage_roles=True)    
@client.command()
async def hideall(ctx):
   for x in ctx.guild.channels:
      await x.set_permissions(ctx.guild.default_role,view_channels=False)


@client.command(aliases=["ui"])
async def userinfo(ctx, member: 
discord.Member = None):
    if member == None:
        member = ctx.author
    if member == '':
        member = ctx.author
    format = "%d-%m-%Y"
    member = ctx.author if not member else member
    member_roles = len(member.roles)
    serverinfo = discord.Embed(colour=discord.Colour(0xff0000))
    serverinfo.add_field(name=" Username", value=f"```{member}```" , inline= False)
    serverinfo.add_field(name=" User ID", value=f"```{member.id}```", inline= False)
    serverinfo.add_field(name=" Created At", value=f"```{member.created_at.strftime(format)}```", inline= False)
    serverinfo.add_field(name=" Joined At", value=f"```{member.joined_at.strftime(format)}```", inline= False)
    serverinfo.add_field(name=" Roles", value=f"```{member_roles}```", inline= False)
    serverinfo.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=serverinfo)

@client.command(aliases=['si'], colour=discord.Colour(0xff0000))
async def serverinfo(ctx):
  guild_roles = len(ctx.guild.roles)
  guild_categories = len(ctx.guild.categories) 
  guild_members = len(ctx.guild.members)
  text_channels = len(ctx.guild.text_channels)
  voice_channels = len(ctx.guild.voice_channels)
  channels = text_channels + voice_channels
  serverinfo = discord.Embed(colour=00000)
  serverinfo.add_field(name=" Server Name", value=f"```{ctx.guild.name}```" , inline = False)
  serverinfo.add_field(name=" Server ID", value=f"```{ctx.guild.id}```", inline = False)
  serverinfo.add_field(name=" Server Owner", value=f"```{ctx.guild.owner}```", inline = False)
  serverinfo.add_field(name=" Boosts", value=f"```{ctx.guild.premium_subscription_count}```", inline = False)
  serverinfo.add_field(name=" Channels", value=f"```{channels}```", inline = False)
  serverinfo.add_field(name=" Roles", value=f"```{guild_roles}```", inline = False)
  serverinfo.add_field(name=" Categories", value=f"```{guild_categories} Categories```", inline = False)
  serverinfo.add_field(name=" Members", value=f"```{guild_members}```", inline = False)
  serverinfo.set_thumbnail(url=ctx.guild.icon_url)
  await ctx.send(embed=serverinfo)

@client.command()
async def invites(ctx):
    totalInvites = 0
    for i in await ctx.guild.invites():
        if i.inviter == ctx.author:
            totalInvites += i.uses
    await ctx.send(f"You've invited {totalInvites} members to the server!")



@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=100):
    await ctx.channel.purge(limit=amount+1)
    await ctx.channel.send("Successfully Cleared Messages")
#@client.event
#async def on_member_join(member):
#  guild = client.get_guild(966920536850571304)
#  cnl = guild.get_channel(975246663268569159)
 # message = await cnl.send(f"{member.mention} welcome to NukeZ ")

#@client.command()
#async def syncofficials(ctx):
  #  guild = client.get_guild(966920536850571304)
  #  role = guild.get_role(978969579722244166)
 #   memberrrr = 0
 #   if ctx.author.top_role.position > ctx.guild.me.top_role.position or ctx.author == ctx.guild.owner:
   #     try:
   #         message = await ctx.reply(f'Adding Officials Role to everyone with **`NukeZ`** in name')
  #          for member in ctx.guild.members:
    #            if 'NukeZ' in str(member.name):
   #                 memberrrr += 1
  #                  await member.add_roles(role)
  #          await message.edit(
 #               content=f'Successfully added roles to {memberrrr} officials!')
#        except:
 #           pass
#    else:
 #     await ctx.reply(f'You must have role above me to use this command.')

#@client.command()
#async def officialcount(ctx):
   # guild = client.get_guild(966920536850571304)
   # role = guild.get_role(978969579722244166)
  #  embed = discord.Embed(title="**Officials Count of NukeZ**",
  #                        description=f"**{len(role.members)} supporters!**",
 #                         color=00000)
 #   await ctx.reply(embed=embed)

#@client.event
#async def on_message(message):
 #   await client.process_commands(message)
   # if message.content.startswith('tag'):
   #     await message.reply(f"**NukeZ**")
 #   if message.content.startswith('Tag'):
  #      await message.reply(f"**NukeZ**")




async def GetMessage(
    bot, ctx, contentOne="Default Message", contentTwo="\uFEFF", timeout=100
):
    """
    This function sends an embed containing the params and then waits for a message to return
    Params:
     - bot (commands.Bot object) :
     - ctx (context object) : Used for sending msgs n stuff
     - Optional Params:
        - contentOne (string) : Embed title
        - contentTwo (string) : Embed description
        - timeout (int) : Timeout for wait_for
    Returns:
     - msg.content (string) : If a message is detected, the content will be returned
    or
     - False (bool) : If a timeout occurs
    """
    embed = discord.Embed(title=f"{contentOne}", description=f"{contentTwo}",)
    sent = await ctx.send(embed=embed)
    try:
        msg = await bot.wait_for(
            "message",
            timeout=timeout,
            check=lambda message: message.author == ctx.author
            and message.channel == ctx.channel,
        )
        if msg:
            return msg.content
    except asyncio.TimeoutError:
        return False


def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content

import datetime
import io
import contextlib
import textwrap

os.system("pip install buttons")

from discord.ext.buttons import Paginator




class Pag(Paginator):
    async def teardown(ctx):
        try:
            await ctx.page.clear_reactions()
        except discord.HTTPException:
            pass

from traceback import format_exception


@commands.check(botowner)
@client.command(name="eval", aliases=["exec", "execute", "luci"])
async def _eval(ctx, *, code):
    code = clean_code(code)

    local_variables = {
        "discord": discord,
        "commands": commands,
        "bot": client,
        "token": token,
        "client": client,
        "ctx": ctx,
        "channel": ctx.channel,
        "author": ctx.author,
        "guild": ctx.guild,
        "message": ctx.message,
    }

    stdout = io.StringIO()

    try:
        with contextlib.redirect_stdout(stdout):
            exec(
                f"async def func():\n{textwrap.indent(code, '    ')}",
                local_variables,
            )

            obj = await local_variables["func"]()
            result = f"{stdout.getvalue()}\n-- {obj}\n"

    except Exception as e:
        result = "".join(format_exception(e, e, e.__traceback__))

    pager = Pag(
        timeout=180,
        use_defaults=True,
        entries=[result[i : i + 2000] for i in range(0, len(result), 2000)],
        length=1,
        prefix="```py\n",
        suffix="```",
    )

    await pager.start(ctx)



@_eval.error
async def _eval_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.reply("You Can't Use This Command")



 
#with open("blacklist.json", "r") as f:

#@client.event
#async def on_command_error(ctx, error):
 # idk = discord.utils.get(message.guild.roles, id=948948865984393226) 

  #if ctx.author.id in [969192890205110313]:
  #  pass
  #else:
  #  embed = discord.Embed(color=0000, title='Titanium Security', description=f"**Command Not Found. Type `_help` for more info.**")
  #  await ctx.reply(embed=embed, mention_author=True)

@client.event
async def on_message(message):
    await client.process_commands(message)
    role = "<@&"
    member = message.author
    guild = message.guild
    if role in message.content:
     if member == guild.owner.id:
        pass 
     else: 
         await message.delete()
         await member.ban(reason="Titanium security | Anti Role Ping")
  #  if message.mention_everyone:
     # if member == guild.owner:
      #  pass
   # else:
     # await message.delete()
     # await member.kick(reason="Titanium Security | Mentioning everyone/here")

@client.command()
async def features(ctx):
    embed = discord.Embed(title=f'Features',
                                description=f"<a:ok:979309565847949342> Anti Bot \n <a:ok:979309565847949342> Anti Ban \n <a:ok:979309565847949342> Anti Kick \n <a:ok:979309565847949342> Anti Prune \n <a:ok:979309565847949342> Anti Channel Create/Delete/Update \n <a:ok:979309565847949342> Anti Role Create/Delete/Update \n <a:ok:979309565847949342> Anti Webhook Create \n <a:ok:979309565847949342> Anti Emoji Create/Delete/Update \n <a:ok:979309565847949342> Anti Invite Delete \n <a:ok:979309565847949342> Anti Guild Update \n <a:ok:979309565847949342> Anti Community Spam \n <a:ok:979309565847949342> Anti Integration Create \n <a:ok:979309565847949342> Anti Role Ping \n <a:ok:979309565847949342> Anti Selfbot \n <a:ok:979309565847949342> 17. Anti Vanity Steal", inline=False) 
    await ctx.reply(embed=embed, mention_author=True)

@client.event
async def on_command_error(ctx, error: commands.CommandError):
  embed1 = discord.Embed(description=f" You are missing the needed `Permissions` to perform this command", color=00000)
  embed2 = discord.Embed(description=f" You are missing the needed `Arguments` to perform this command", color=00000)
  embed3 = discord.Embed(description=f"The selected `Member` could not be found", color=00000)
  embed4 = discord.Embed(description=f" I am missing the needed `Permissions` to perform this command", color=00000)
  embed5 = discord.Embed(description=f" This command is on a cooldown, please try again in `2` seconds.", color=00000)
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(embed=embed1)
  elif isinstance(error, commands.MissingRequiredArgument):
     await ctx.send(embed=embed2)
  elif isinstance(error, commands.MemberNotFound):
    await ctx.send(embed=embed3)
  elif isinstance(error, commands.BotMissingPermissions):
    await ctx.send(embed=embed4)
  elif isinstance(error, commands.CommandOnCooldown):
    await ctx.send(embed=embed5)
  else:
    raise error
  
client.run(token)