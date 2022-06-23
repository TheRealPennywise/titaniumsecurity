
import asyncio
import math
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from discord_components import DiscordComponents, Button, ButtonStyle




class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        DiscordComponents(bot)


    @commands.command(aliases=['Help','h'])
    async def help(self, ctx):
        embed = discord.Embed(color=000000, title="Titanium Security")
        embed.add_field(name=f"Help menu", value=f"• My Prefix **_**\n• [Get Titanium](https://discord.com/api/oauth2/authorize?client_id=980052857493553202&permissions=8&scope=bot) | [Support Server](https://discord.gg/nukez)")
        embed.add_field(name="Titanium Commands", value="<a:Antinuke:978543289936523275> Antinuke \n <a:Antinuke:978543289936523275> Giveaway \n <a:Antinuke:978543289936523275> Features \n <a:Antinuke:978543289936523275> Moderation")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/979324418276864000/980038708222894150/images_3.jpeg")
        embed2 = discord.Embed(title=f'Antinuke Commands',
                                description=f"<:reflex_dot:979308978163048448>**Features** \n<:reflex_dot:979308978163048448>**Massunban** \n<:reflex_dot:979308978163048448>**Recover** \n<:reflex_dot:979308978163048448>**Channelclean**\n<:reflex_dot:979308978163048448>**Roleclean**", inline=False)

        embed3 = discord.Embed(title=f'Giveaway Commands',
                                description=f"<:reflex_dot:979308978163048448>**Gstart** \n<:reflex_dot:979308978163048448>**Greroll**", inline=False)  

        embed4 = discord.Embed(title=f'Features',
                                description=f"<a:ok:979309565847949342> Anti Bot \n <a:ok:979309565847949342> Anti Ban \n <a:ok:979309565847949342> Anti Kick \n <a:ok:979309565847949342> Anti Prune \n <a:ok:979309565847949342> Anti Channel Create/Delete/Update \n <a:ok:979309565847949342> Anti Role Create/Delete/Update \n <a:ok:979309565847949342> Anti Webhook Create \n <a:ok:979309565847949342> Anti Emoji Create/Delete/Update \n <a:ok:979309565847949342> Anti Invite Delete \n <a:ok:979309565847949342> Anti Guild Update \n <a:ok:979309565847949342> Anti Community Spam \n <a:ok:979309565847949342> Anti Integration Create \n <a:ok:979309565847949342> Anti Role Ping \n <a:ok:979309565847949342> Anti Selfbot \n <a:ok:979309565847949342> 17. Anti Vanity Steal", inline=False) 

        embed5 = discord.Embed(title=f'Mod Commands',
                                description=f"<:btt_EC_ban:979309633455947806> Kick \n <:btt_EC_ban:979309633455947806> Ban \n <:btt_EC_ban:979309633455947806> Clear \n <:btt_EC_ban:979309633455947806> Unban  \n <:btt_EC_ban:979309633455947806> Slowmode \n <:btt_EC_ban:979309633455947806> Unslow \n <:btt_EC_ban:979309633455947806> Hackban", inline=False)  
   # await ctx.reply(embed=embed, mention_author=True)
        paginationList = [embed, embed2, embed3, embed4, embed5]
        current = 0
        mainMessage = await ctx.send(
            embed = paginationList[current],
            components = [
                [
                    Button(
                        label = "◄",
                        id = "back",
                        style = 1
                    ),
                    Button(
                        label = "►",
                        id = "front",
                        style = 1
                    )
                ]
            ]
        )
        while True:
            try:
                interaction = await self.bot.wait_for(
                    "button_click",
                    check = lambda i: i.component.id in ["back", "front"],
                    timeout = 15.0
                )
                if interaction.component.id == "back":
                    current -= 1
                elif interaction.component.id == "front":
                    current += 1
                if current == len(paginationList):
                    current = 0
                elif current < 0:
                    current = len(paginationList) - 1

                await interaction.respond(
                    embed = paginationList[current],
                    components = [
                        [
                            Button(
                                label = "◄",
                                id = "back",
                                style = 1
                            ),
                            Button(
                                label = "►",
                                id = "front",
                                style = 1
                            )
                        ]
                    ]
                )
            except asyncio.TimeoutError:
                await mainMessage.edit(
                    components = [
                        [
                            Button(
                                label = "◄",
                                id = "back",
                                style = 1,
                                disabled = True
                            ),
                            Button(
                                label = "►",
                                id = "front",
                                style = 1,
                                disabled = True
                            )
                        ]
                    ]
                )
                break

def setup(bot):
    bot.add_cog(Help(bot))          