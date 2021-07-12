import discord
from discord.ext import commands

class Administracion(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} Se ha unido :D')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} Nos abandono D:')

    @commands.command(aliases = ['Kick'])
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'E kickeado a: {member.mention}')

    @commands.command(aliases = ['Ban'])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'E baneado a: {member.mention}')

    @commands.command(aliases = ['Unban'])
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Usuario {user.mention} fue desbaneado')
                return

    @commands.command(aliases = ['Vaciar'])
    @commands.has_permissions(administrator=True)
    async def vaciar(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(Administracion(client))