from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        """Erase a certain amount of messages."""
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{amount} messages have been erased", delete_after=5)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason=None):
        """ Kick a member from the server."""
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} has been kicked.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        """Ban a member from the server."""
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} has been banned.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        """Unban a member from the server."""
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            if user.name == member:
                await ctx.guild.unban(user)
                await ctx.send(f"{user.mention} has been unbanned.")
                return

        await ctx.send(f"{member} is not banned.")

def setup(client):
    return client.add_cog(Moderation(client))