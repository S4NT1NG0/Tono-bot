import discord
from discord.ext import commands

class Extra(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def ayuda(self, ctx):
        await ctx.send('```Soy TonoBot! Aqui mis comandos actuales, Sigo estando sin terminar asi que, sientete libre de sugerir que deberia de saber hacer! :D```')
        await ctx.send('```\n\nDiversion:\n\nBola8 (B8) - Si quieres hacer una pregunta a la que no tienes respuesta\nPing - Para checar mi ping actual\nGolpear @Persona - Por si tienes asuntos sin resolver con esa persona que te cae mal >:D\nMatar (Masacrar) - Por si quieres matar a alguien.. D:\nwaifu - comando para ver alguna waifu de anime (peticion de daniel)```')
        await ctx.send('```Administracion:\n\nKick - Para sacar a la gente temporalmente\nBan - Para prohibir a la gente de entrar al servidor indefinidamente\nUnban - Para permitir que la gente baneada vuelva al servidor```')

def setup(client):
    client.add_cog(Extra(client))