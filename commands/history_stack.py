from discord.ext import commands
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from lib.stack import Stack

class HistoryStack(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.history = Stack('history') # history of commands

    @commands.command()
    async def history_head(self, ctx): # print the first command of the history
        """Print the first command of the history."""
        await ctx.send(self.history.peek())
        
    @commands.command()
    async def history_next(self, ctx):
        """Print the next command of the history."""
        if self.history.get_index() < self.history.get_size()-1:
            print(self.history.get_index(), "index", self.history.get_size(), "size")
            self.history.increment_index()
            await ctx.send(self.history.print_index(self.history.get_index()))
        else:
            await ctx.send("No next command")
        
    @commands.command()
    async def history_previous(self, ctx):
        """Print the previous command of the history."""
        if self.history.get_index() > 0:
            print(self.history.get_index(), "index", self.history.get_size(), "size")
            self.history.increment_index()
            await ctx.send(self.history.print_index(self.history.get_index()))
        else:
            await ctx.send("No previous command")
    
    @commands.command()       
    async def history_clear(self, ctx):
        """Clear the history of commands."""
        await ctx.send(self.history.clear())
        await ctx.send("History cleared")
    
    @commands.command()     
    async def print_history_index(self, ctx):
        """Print the command at the index given by the user."""
        await ctx.send("Please enter your input:")
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel # check if the message is from the same author and channel as the command message
        msg = await client.wait_for("message", check=check)
        if msg.content.isdigit():
            await ctx.send(self.history.print_index(msg.content))
            
    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        """Save the command in the history."""
        blacklist = ['history_head', 'history_next', 'history_previous', 'history_clear', 'print_history_index']
        if ctx.author.bot or ctx.command.name in blacklist:
            return

        self.history.push(ctx.command.name)

            
def setup(client):
    return client.add_cog(HistoryStack(client))