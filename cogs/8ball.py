import discord
from discord.ext import commands
from replit import db
import random

class _8ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball', '8b'])
    async def _8ball(self, ctx, question):
        responses = [ "Yes.",
                      "No.",
                      "My sources say yes",
                      "Most likely.",
                      "idk",
                      "bruh",
                      "k",
                      "nah",
                      "-__-",
                      "maybe sometime",
                      "Outlook good.",
                      "Signs point to yes.",
                      "Helo?? Anybody home??!!??",
                      "Definitely",
                      "Absolutely",
                      "Nope.",
                      "No thanks, I won’t be able to make it.",
                      "No Way!",
                      "It is certain.",
                      "It is decidedly so.",
                      "Without a doubt.",
                      "Definitely yes.",
                      "You may rely on it.",
                      "As I see it, yes.",
                      "I hope so..",
                      "Is trump's skin orange?",
                      "Not even in your dreams",
                      "No, you dingleberry",
                      "Why would you even think about it",
                      "Try again later",
                      "ask again later",
                      "Never..",
                      "Who even cares?",
                      "Sorry... but no",
                      "Probably"]

        response = random.choice(responses)
      
        await ctx.send(f'{response}')

def setup(client: commands.Bot):
    client.add_cog(_8ball(client))