import discord
from discord.ext import commands
import random

class Diversion(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['lag', 'check'])
    async def ping(self, ctx):
        await ctx.send(f'{round(commands.bot.latency * 1000)}ms')

    @commands.command(aliases = ['B8', 'Bola8'])
    async def  _Bola8(self, ctx, *, question):
       respuestas = [
           'No', 'Puede ser', 'Las estrellas dicen que no',
            'Lo dudo', 'Definitivamente', 'Parece que si',
            'Todo apunta a que si', 'Consentrate y pregunta denuevo',
           'Yo pienso que no..', 'Definitivamente.. no.', 'Nunca'
            ]
    
       await ctx.send(f'```Pregunta: {question}\nRespuesta: {random.choice(respuestas)}```')
    
    @commands.command(alias = ['Golpear'])
    async def golpear(self, ctx, *, member:discord.Member):
        gif_list = [
            'https://tenor.com/view/anime-naruto-punch-fight-gif-12911685',
            'https://tenor.com/view/tgggg-anime-punch-gif-13142581',
            'https://tenor.com/view/one-punch-man-saitama-anime-punch-gif-17053376',
            'https://tenor.com/view/punch-combo-gif-18354923',
            'https://tenor.com/view/tokyo-revengers-anonymouskun-anime-punch-angry-gif-21853753',
            'https://tenor.com/view/anime-punch-mad-angry-gif-15580060'
        ]

        await ctx.send(f'{ctx.author.name} Golpeo a {member}\n{random.choice(gif_list)}')

    @commands.command(alias = ['Masacrar'])
    async def matar(self, ctx, *, member:discord.Member):
        kill_gifs = [
            'https://tenor.com/view/rifle-shooting-slow-motion-gif-20582439',
            'https://tenor.com/view/shooting-practicing-targeting-anime-gun-gif-17216777',
            'https://tenor.com/view/anime-shooting-gun-shoot-firing-gif-8118409',
            'https://tenor.com/view/fat-guy-shooting-gun-gun-shot-gif-15114243',
            'https://tenor.com/view/id-invaded-gun-anime-shoot-kill-gif-16663051'
            ]

        await ctx.send(f'{ctx.author.name} a matado a {member} D:\n{random.choice(kill_gifs)}')

def setup(client):
    client.add_cog(Diversion(client))