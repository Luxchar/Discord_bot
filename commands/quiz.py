from discord.ext import commands
import sys
sys.path.append("..") # Adds higher directory to python modules path.

from lib.hashtable_user import Hashtable_user
from lib.tree import Tree

import asyncio

class Quiz(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.tree = self.create_tree()
        
    def create_tree(self) -> Tree:
        """Create the tree of questions and answers"""
        tree = Tree('Do you wanna play a team sport or an individualist sport ?') # create the tree
        tree.append_question('Do you wanna play a sport with a ball or without a ball ? Answer: "team" or "individualist"', ['team'], 'Do you wanna play a team sport or an individualist sport ?')
        tree.append_question('Do you wanna play a sport with a racket or without a racket ? Answer: "racket" or "without"', ['individualist'], 'Do you wanna play a team sport or an individualist sport ?')
        
        tree.append_question('Do you wanna play football or basket ?  Answer: "football" or "basket"', ['ball'], 'Do you wanna play a sport with a ball or without a ball ?')
        tree.append_question('Do you wanna play tennis or badminton ?  Answer: "tennis" or "badminton"', ['racket'], 'Do you wanna play a sport with a racket or without a racket ?')
        tree.append_question('Do you prefer running or swimming ?  Answer: "running" or "swimming"', ['without'], 'Do you wanna play a sport with a ball or without a ball ?')
        tree.append_question('Do you prefer weightlifting or crossfit - Answer: "weightlifting" or "crossfit"', ['without'], 'Do you wanna play a sport with a racket or without a racket ?')
        
        tree.append_question('Great choice football is a very famous sport for a reason !', ['football'], 'Do you wanna play football or basket ?')
        tree.append_question('Great choice basket is a very famous sport for a reason !', ['basket'], 'Do you wanna play football or basket ?')
        tree.append_question('Great choice tennis is a very famous sport for a reason !', ['tennis'], 'Do you wanna play tennis or badminton ?')
        tree.append_question('Great choice badminton is a very famous sport for a reason !', ['badminton'], 'Do you wanna play tennis or badminton ?')
        tree.append_question('Great choice running is a very famous sport for a reason !', ['running'], 'Do you prefer running or swimming ?')
        tree.append_question('Great choice swimming is a very famous sport for a reason !', ['swimming'], 'Do you prefer running or swimming ?')
        tree.append_question('Great choice weightlifting is a very famous sport for a reason !', ['weightlifting'], 'Do you prefer weightlifting or crossfit ?')
        tree.append_question('Bad choice try again', ['crossfit'], 'Do you prefer weightlifting or crossfit ?')
        
        return tree
        
    @commands.command()
    async def play(self, ctx):
        """Start the game"""
        await ctx.channel.send("Do you wanna play a team sport or an individualist sport ?")
        
    @commands.command()
    async def reset(self, ctx):
        """Reset the game"""
        self.tree = await self.create_tree()
        await ctx.channel.send("Do you wanna play a team sport or an individualist sport ?")
        
    @commands.command()
    async def speak_about(self, ctx, arg):
        """Does the bot speak about the topic"""
        await ctx.channel.send(self.tree.speak_about(arg))
        
    @commands.command()
    async def answer(self, ctx, arg):
        """Answer the question of the bot"""
        answer = self.tree.send_answer(arg)
        if answer == None:
            await ctx.channel.send("I don't understand your answer, please try again")
            return
        await ctx.channel.send(answer)

def setup(client):
    return client.add_cog(Quiz(client))