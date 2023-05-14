import random
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def rps(self, ctx, choice):
        """Play a game of rock, paper, scissors with the bot."""
        options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(options)
        if choice.lower() not in options:
            await ctx.send("That's not a valid choice!")
        elif choice.lower() == computer_choice:
            await ctx.send(f"We both chose {choice}! It's a tie.")
        elif (choice.lower() == 'rock' and computer_choice == 'scissors') or \
             (choice.lower() == 'paper' and computer_choice == 'rock') or \
             (choice.lower() == 'scissors' and computer_choice == 'paper'):
            await ctx.send(f"I chose {computer_choice}. You win!")
        else:
            await ctx.send(f"I chose {computer_choice}. I win!")
    
    @commands.command()
    async def flip(self, ctx):
        """Flip a coin and get heads or tails."""
        result = random.choice(['heads', 'tails'])
        await ctx.send(f"The coin landed on {result}!")
    
    @commands.command()
    async def guess(self, ctx, num):
        """Guess a random number between 1 and 10."""
        answer = random.randint(1, 10)
        try:
            guess = int(num)
        except ValueError:
            await ctx.send("That's not a valid number!")
            return
        if guess < 1 or guess > 10:
            await ctx.send("Your guess must be between 1 and 10.")
        elif guess == answer:
            await ctx.send("You got it!")
        else:
            await ctx.send(f"Sorry, the number was {answer}.")
            
def setup(client):
    return client.add_cog(Games(client))
