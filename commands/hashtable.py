from discord.ext import commands
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from lib.hashtable_user import Hashtable_user

class Hashtable(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.history2 = Hashtable_user(10) # create a queue for users to access the bot

    @commands.command()
    async def history2_print(self, ctx):
        """Show the history of the user."""
        user = history2.get_history(ctx.author.id)
        if user is None:
            await ctx.send("You don't have any history")
        else:
            await ctx.send(user)

def setup(client):
    return client.add_cog(Hashtable(client))