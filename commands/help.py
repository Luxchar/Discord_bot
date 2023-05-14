from discord.ext import commands

class Help(commands.HelpCommand):
    def __init__(self, **options):
        super().__init__(**options)

    async def send_bot_help(self, mapping):
        ctx = self.context
        command_list = []

        for cog in self.context.bot.cogs.values():
            command_list.extend(cog.get_commands())

        help_text = "Liste des commandes :\n"
        for command in command_list:
            help_text += f" - {command.name} : {command.help}\n"

        await ctx.send(f"```{help_text}```")
        
    async def ping(self, ctx):
        """Ping the bot."""
        await ctx.send("pong")

async def setup(bot):
    bot.help_command = Help()