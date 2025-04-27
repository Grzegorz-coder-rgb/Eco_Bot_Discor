import discord
from bot_logic import *
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
    print("Porada: Użyj $rec_help")

@bot.command()
async def rec_help(ctx):
    await ctx.send("Oto komendy dotyczące recyklingu:\n- $rec_pomysl\n- $dodaj_pomysl <pomysł>\n- $rec_informacje" )

@bot.command()
async def rec_pomysl(ctx):
    await ctx.send(recl_pomysl())  # Wywołanie funkcji z bot_logic.py

@bot.command()
async def dodaj_pomysl(ctx, *, pomysl):  # Dodano *, aby obsłużyć wielowyrazowe pomysły
    odp = new_pomysl(pomysl)
    await ctx.send(odp)

@bot.command()
async def rec_informacje(ctx):
    wynik = rec_rozklad()
    await ctx.send(f"Czas rozkładu różnych odpadów:\n{wynik}")

bot.run("")#Token bota

