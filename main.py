# Todo esto es lo principal, basicamente un cog para conectar todos los comandos utiles
# sientete libre de mostrarselo a alguien mas solo recuerda no darles la token tony, o si no podrian
# hacker la cuenta, habiendo dicho esto, esto es el "Source Code" de el bot, si no sabes lo que haces
# sientete libre de googlearlo, o solo no lo edites, si le quieres agregar algo dime.

from operator import truediv
import discord
from discord import activity
from discord.ext import commands
import random
import os
from discord.ext import tasks
from itertools import cycle
import waifus

client = commands.Bot(command_prefix = 't!')
estado = [
    'Escuchando a la gente.. ( t!ayuda ) para recibir ayuda XD',
    'El mejor bot de la historia de la humanidad.. ( t!ayuda ) por si quieres ayuda',
    'El bot que siempre te escucha! :D  ( t!ayuda ) si gustas ser auxiliado',
    'Escribe ( t!ayuda ) para no ver al mundo arder',
    'El unico bot que te ve mientras duermes 0.0 ( t!ayuda )'
]
status = cycle(estado)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    change.start()
    print("TonoBot en linea")

@tasks.loop(seconds=30)
async def change():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def waifu(ctx):
    await ctx.send(f'Aqui tienes tu waifu: {random.choice(waifus.waifu_list)}')

client.run('ODYyNzg4Mzc1NTYyOTQ0NTMz.YOdcSg.swZ0wiIj0MSUfAVEbg7PLcLgmmE')