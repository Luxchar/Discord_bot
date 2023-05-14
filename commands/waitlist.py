from discord.ext import commands
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from lib.queue import Queue

class Waitlist(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.queue = Queue('queue:') # create a queue for users to access the bot
        
    async def manage_queue(self):
        """Manage the queue of users to access the bot."""
        await self.client.wait_until_ready() # wait until the bot is ready
        while not self.client.is_closed(): # while the bot is running
            if self.queue.len() > 0: # if there are users in the queue
                user = self.queue.dequeue() # get the first user in the queue
                await user
            await asyncio.sleep(5)

    @commands.command()   
    async def add_to_queue(self, user):
        """Add the user to the queue."""
        self.queue.enqueue(user)
        await user.send("You have been added to the queue. Please wait for your turn.")


def setup(client):
    return client.add_cog(Waitlist(client))