import discord
from discord.ext import commands
from discord import Embed, Member
from replit import db


class userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx):
        """View the info of a user."""
        target = ctx.message.author or ctx.message.mentions[0]
        userinfo = discord.Embed(
            title=f"User info of {target}",
            color=discord.Color.blue(),
        )
    
        userinfo.add_field(name="Name", value=str(target), inline=True)

        userinfo.add_field(name="User ID", value=target.id, inline=True)

        userinfo.add_field(name="Created at", value=target.created_at.strftime("%d/%m/%Y %H:%M:%S"), inline=True)

        userinfo.add_field(name="Joined at", value=target.joined_at.strftime("%d/%m/%Y %H:%M:%S"), inline=True)


        userinfo.set_thumbnail(url=target.avatar_url)

        await ctx.send(embed=userinfo)
      

def setup(client: commands.Bot):
    client.add_cog(userinfo(client))