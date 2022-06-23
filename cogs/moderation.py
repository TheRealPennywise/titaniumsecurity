import discord
import time
import pymongo
import os
from discord import User, errors
import re
import typing
import typing as t
from discord.ext.commands import has_permissions, MissingPermissions, has_role, has_any_role
import asyncio
from datetime import datetime

from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"[\x1b[38;5;213mLOG\x1b[38;5;15m] Cog Loaded: [\x1b[38;5;213m{self.__class__.__name__}\x1b[38;5;15m]")

    # Commands          
    @commands.group(aliases=["mod"])
    @commands.guild_only()
    
    
    async def moderation(self, ctx):
        embed = discord.Embed(color=000000)
        embed.add_field(name=f"Moderation", value=f"<:btt_EC_ban:979309633455947806> Kick \n <:btt_EC_ban:979309633455947806> Ban \n <:btt_EC_ban:979309633455947806> Clear \n <:btt_EC_ban:979309633455947806> Unban  \n <:btt_EC_ban:979309633455947806> Slowmode \n <:btt_EC_ban:979309633455947806> Unslow \n <:btt_EC_ban:979309633455947806> Hackban \n <:btt_EC_ban:979309633455947806> Lock \n <:btt_EC_ban:979309633455947806> Unlock \n <:btt_EC_ban:979309633455947806> Hide \n <:btt_EC_ban:979309633455947806> Unhide \n <:btt_EC_ban:979309633455947806> Roleinfo \n <:btt_EC_ban:979309633455947806> Hideall \n <:btt_EC_ban:979309633455947806> Unhideall \n <:btt_EC_ban:979309633455947806> Setvanity \n <:btt_EC_ban:979309633455947806> Userinfo \n <:btt_EC_ban:979309633455947806> Serverinfo \n <:btt_EC_ban:979309633455947806> Invites \n <:btt_EC_ban:979309633455947806> Purge")
        await ctx.reply(embed=embed, mention_author=True)


      
    @commands.command(
        name='kick',
        description='Kick someone from the server',
        usage='`.kick [@user]`'
    )
    @commands.cooldown(3, 14, BucketType.user)
    
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        if ctx.author == member:
            await ctx.reply(
                embed = discord.Embed(description=f" You cannot kick yourself\n", color=00000))
        elif ctx.author.top_role < member.top_role:
            await ctx.reply(embed = discord.Embed(description=f" You cannot kick a member above you\n", color=00000))
        elif ctx.guild.owner == member:
            await ctx.reply(
                embed = discord.Embed(description=f" You cannot kick the guild owner\n", color=00000))
        else:
            if reason == None:
                try:
                    try:
                        await member.kick()
                        await ctx.reply(embed= discord.Embed(description=f" Successfully kicked {member.mention}", color=00000))
                    except:
                        await member.kick()
                        await ctx.reply(embed= discord.Embed(description=f" Successfully kicked {member.mention}", color=00000))
                except:
                    await ctx.reply(embed = discord.Embed(description=f" I could not kick {member.mention}\n", color=00000))
            else:
                try:

                    await member.kick(reason=reason)
                    await ctx.reply(embed= discord.Embed(description=f" Successfully kicked {member.mention} for {reason}", color=00000))
                except:
                    await ctx.reply(embed = discord.Embed(description=f" I could not kick {member.mention}\n", color=00000))
                
    @commands.command(
        name='ban',
        description='Kick someone from the server',
        usage='`.kick [@user]`'
    )
    @commands.cooldown(3, 14, BucketType.user)
    
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        if ctx.author == member:
            await ctx.reply(
                embed = discord.Embed(description=f" You cannot ban yourself\n", color=00000))
        elif ctx.author.top_role < member.top_role:
            await ctx.reply(embed = discord.Embed(description=f" You cannot ban a member above you\n", color=00000))
        elif ctx.guild.owner == member:
            await ctx.reply(
                embed = discord.Embed(description=f" You cannot ban the guild owner\n", color=00000))
        else:
            if reason == None:
                try:
                    try:
                        await member.ban()
                        await ctx.reply(embed= discord.Embed(description=f" Successfully banned {member.mention}", color=00000))
                    except:
                        await member.ban()
                        await ctx.reply(embed= discord.Embed(description=f" Successfully banned {member.mention}", color=00000))
                except:
                    await ctx.reply(embed = discord.Embed(description=f" I could not ban {member.mention}\n", color=00000))
            else:
                try:

                    await member.ban(reason=reason)
                    await ctx.reply(embed= discord.Embed(description=f" Successfully banned {member.mention} for {reason}", color=00000))
                except:
                    await ctx.reply(embed = discord.Embed(description=f" I could not ban {member.mention}\n", color=00000))

    @commands.command(
        name='unban',
        description='Unbans the specified user.',
        usage='`.unban [@user]`'
    )
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(3, 14, BucketType.user)
    
    async def unban(self, ctx, userid, reason=None):

        if ctx.author == userid:
            await ctx.reply(embed = discord.Embed(description=f" You cannot unban yourself\n", color=00000))
        else: 
            try:
               user = discord.Object(id=userid)
               await ctx.guild.unban(user)
               await ctx.reply(embed= discord.Embed(description=f" Successfully unbanned {userid} for {reason}", color=00000))
            except:
                await ctx.reply(embed = discord.Embed(description=f" I could not unban that user\n", color=00000))


    @commands.group(aliases=["c"])
    @commands.guild_only()
    @commands.max_concurrency(1, per=commands.BucketType.guild)
    
    async def clear(self, ctx):
        embed = discord.Embed(color=000000)
        embed.add_field(name=f"Clear <cmd>", value=f"<:reflex_dot:979308978163048448> Clear all \n <:reflex_dot:979308978163048448> Clear bots \n <:reflex_dot:979308978163048448> Clear embeds \n <:reflex_dot:979308978163048448> Clear files \n <:reflex_dot:979308978163048448> Clear mentions \n <:reflex_dot:979308978163048448> Clear images \n <:reflex_dot:979308978163048448> Clear contains \n <:reflex_dot:979308978163048448> Clear reactions")
        await ctx.reply(embed=embed, mention_author=True)
    async def do_removal(self, ctx, limit, predicate, *, before=None, after=None, message=True):
        if limit > 2000:
            em = discord.Embed(description=f" Too many messages to search given ({limit}/2000)", color=00000, delete_after=3)
            return await ctx.send(embed=em)

        if not before:
            before = ctx.message
        else:
            before = discord.Object(id=before)

        if after:
            after = discord.Object(id=after)

        try:
            deleted = await ctx.channel.purge(limit=limit, before=before, after=after, check=predicate)
        except discord.HTTPException as e:
            em = discord.Embed(description=f" Try a smaller search?", color=00000)
            return await ctx.send(embed=em)

        deleted = len(deleted)
        if message is True:
            await ctx.message.delete()
            await ctx.send(embed= discord.Embed(description=f" Successfully removed {deleted} message{'' if deleted == 1 else 's'}.", color=00000, delete_after=3))

    @clear.command(aliases=["e"])
    
    
    async def embeds(self, ctx, search=100):
        """Removes messages that have embeds in them."""
        await self.do_removal(ctx, search, lambda e: len(e.embeds))

    @clear.command(aliases=["f"])
    
    
    async def files(self, ctx, search=100):
        """Removes messages that have attachments in them."""
        await self.do_removal(ctx, search, lambda e: len(e.attachments))

    @clear.command(aliases=["m"])
    
    
    async def mentions(self, ctx, search=100):
        """Removes messages that have mentions in them."""
        await self.do_removal(ctx, search, lambda e: len(e.mentions) or len(e.role_mentions))

    @clear.command(aliases=["i"])
    
    
    async def images(self, ctx, search=100):
        """Removes messages that have embeds or attachments."""
        await self.do_removal(ctx, search, lambda e: len(e.embeds) or len(e.attachments))

    @clear.command(name="all")
    
    
    async def _remove_all(self, ctx, search=100):
        """Removes all messages."""
        await self.do_removal(ctx, search, lambda e: True)

    @clear.command(aliases=["co"])
    
    
    async def contains(self, ctx, *, substr: str):
        """Removes all messages containing a substring.
        The substring must be at least 3 characters long.
        """
        if len(substr) < 3:
            await ctx.send("The substring length must be at least 3 characters.")
        else:
            await self.do_removal(ctx, 100, lambda e: substr in e.content)

    @clear.command(name="bots", aliases=["b"])
    
    
    async def _bots(self, ctx, search=100, prefix=None):
        """Removes a bot user's messages and messages with their optional prefix."""

        getprefix = [";", "$", "!", "-", "?", ">", "^", "$", "w!", ".", ",", "a?", "g!", "m!", "s?"]

        def predicate(m):
            return (m.webhook_id is None and m.author.bot) or m.content.startswith(tuple(getprefix))

        await self.do_removal(ctx, search, predicate)

    @clear.command(name="emojis", aliases=["em"])
    
    
    async def _emojis(self, ctx, search=100):
        """Removes all messages containing custom emoji."""
        custom_emoji = re.compile(r"<a?:(.*?):(\d{17,21})>|[\u263a-\U0001f645]")

        def predicate(m):
            return custom_emoji.search(m.content)

        await self.do_removal(ctx, search, predicate)
        
    @clear.command(name="reactions", aliases=["r"])
    
    
    async def _reactions(self, ctx, search=100):
        """Removes all reactions from messages that have them."""

        if search > 2000:
            return await ctx.send(f"Too many messages to search for ({search}/2000)")

        total_reactions = 0
        async for message in ctx.history(limit=search, before=ctx.message):
            if len(message.reactions):
                total_reactions += sum(r.count for r in message.reactions)
                await message.clear_reactions()
        await ctx.message.delete()
        await ctx.send(embed=discord.Embed(description=f" Successfully removed {total_reactions}.", color=00000, delete_after=3))
    


    
    

            
    @commands.command(usage="@user/id <role_name>")

    
    
    async def role(self, ctx, member: discord.Member, role: discord.Role):
        """Gives member a role.
        role: discord.Role
            The name of the role.
        member: discord.Member
            The member to give the role.
        """
        embed = discord.Embed(color=00000)

        if (
            ctx.author != member
            and ctx.author.top_role <= member.top_role
            and ctx.guild.owner != ctx.author
        ):
            await ctx.reply(embed = discord.Embed(description=f" You can't change the role of someone higher than you\n", color=00000))

        if (
            ctx.author == member
            and ctx.author.top_role <= role
            and ctx.guild.owner != ctx.author
        ):
            await ctx.reply(embed = discord.Embed(description=f" You can't give yourself a role higher than your highest role.\n", color=00000))

        if role in member.roles:
            await member.remove_roles(role)
            embed = discord.Embed(description=f" Successfully removed {member.mention} from {role}", color=00000)
            return await ctx.reply(embed=embed)

        await member.add_roles(role)
        embed = discord.Embed(description=f" Successfully added {role} to {member.mention}", color=00000)
        return await ctx.reply(embed=embed)
            
            
    @commands.command(pass_context=True, usage="<seconds>")
    @commands.cooldown(1, 3, commands.BucketType.user)

    async def slowmode(self, ctx, amount):
        await ctx.channel.edit(slowmode_delay=int(amount))
        await ctx.reply(embed= discord.Embed(description=f" Successfully slowed the channel.", color=00000))
            
    @commands.command(pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.check_any(has_permissions(manage_roles=True), has_any_role("mod", "moderator", "mods", "admin", "staff", "moderators", "+", "adm"))
    async def unslow(self, ctx):
        await ctx.channel.edit(slowmode_delay=0)
        await ctx.reply(embed= discord.Embed(description=f" Successfully unslowed the channel.", color=00000))

    
    @commands.command(
        name="hackban",
        description="Bans a user thats not in the server.",
        usage="`.hackban [id] [reason]`"
    )
    @commands.cooldown(3, 14, BucketType.user)
    
    async def hackban(self, ctx, userid, *, reason=None):

        try:
            userid = int(userid)
        except:
            await ctx.reply(embed = discord.Embed(description=f" You gave a invalid ID, please give a valid ID\n", color=00000))
        
        try:
            await ctx.guild.ban(discord.Object(userid), reason=reason)
            await ctx.reply(embed= discord.Embed(description=f" Successfully hackbanned {userid} for {reason}", color=00000))
        except:
            await ctx.reply(embed = discord.Embed(description=f" I could not Hackban that ID\n", color=00000))
    
    @commands.Cog.listener()
    async def on_message(self, message):
        prefix = "_"
        if str(self.bot.user.id) in message.content:
            embed = discord.Embed(description=f'>>> I am **{self.bot.user.name}**\n • [Get {self.bot.user.name}](https://discord.com/api/oauth2/authorize?client_id=980052857493553202&permissions=8&scope=bot) \n • The prefix for me in this server is: {prefix}\n • Type `{prefix}help` for more info.', color=00000)
            await message.channel.send(embed=embed)
            
 
def setup(bot):
    bot.add_cog(moderation(bot))