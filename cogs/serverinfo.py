import discord
from discord.ext import commands
from replit import db


class serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        """View the info of the server."""

        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        categories = len(ctx.guild.categories)
        channels = text_channels + voice_channels
        role_count = len(ctx.guild.roles)
        emoji_count = len(ctx.guild.emojis)

        serverinfo = discord.Embed(
            title=f"{ctx.guild.name}",
            color=discord.Color.blue()
        )
    
        serverinfo.add_field(name="Server Owner", value=f"{ctx.guild.owner}", inline=True)

        serverinfo.add_field(name="Server Region", value=f"{ctx.guild.region}", inline=True)

        serverinfo.add_field(name="Server ID", value=f"{ctx.guild.id}", inline=False)

        serverinfo.add_field(name="Server created at", value=f"{ctx.guild.created_at}", inline=True)

        serverinfo.add_field(name="Total Members", value=f"{ctx.guild.member_count}", inline=False)

        serverinfo.add_field(name="Channels", value=channels, inline=True)

        serverinfo.add_field(name="Text Channels", value=text_channels, inline=True)

        serverinfo.add_field(name="Voice Channels", value=voice_channels, inline=True)

        serverinfo.add_field(name="Categories", value=categories, inline=True)

        serverinfo.add_field(name="Roles", value=role_count, inline=True)

        serverinfo.add_field(name="Emoji", value=emoji_count, inline=True)

        serverinfo.set_thumbnail(url=f"{ctx.guild.icon_url}")

        await ctx.send(embed=serverinfo)
      

def setup(client: commands.Bot):
    client.add_cog(serverinfo(client))