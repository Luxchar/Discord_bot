from discord.ext import commands
import sys

sys.path.append("..")  # Adds higher directory to python modules path.

from lib.hashtable_user import Hashtable_user

class Hashtable(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.history2 = Hashtable_user(10)  # create a queue for users to access the bot

    @commands.command()
    async def history2_print(self, ctx):
        """Show the history of the user."""
        user = self.history2.get(ctx.author.id)
        if user is None:
            await ctx.send("You don't have any history")
        else:
            await ctx.send(user)

    @commands.Cog.listener()
    async def on_command_completion_hashtable(self, ctx):
        """Save the command in the history of the user."""
        blacklist = ['history_head', 'history_next', 'history_previous', 'history_clear', 'print_history_index']
        if ctx.author.bot or ctx.command.name in blacklist:
            return

        self.history2.append(ctx.author.id, ctx.command.name)
        
def setup(client):
    return client.add_cog(Hashtable(client))