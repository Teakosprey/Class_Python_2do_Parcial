#MTA4MjI5MTA4MTc0NTU0NzQwNA.GukbI4.92b11VG_TsOFtU_o0KKmLUAMvvfIZZLIIgv0g8
import os
import pytube
import openai
import discord
from discord.ext import commands

TOKEN = "MTA4MjI5MTA4MTc0NTU0NzQwNA.GukbI4.92b11VG_TsOFtU_o0KKmLUAMvvfIZZLIIgv0g8"
openai.api_key = "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"

intents = discord.Intents.default()
client = discord.Client(intents = intents)

@client.event
async def on_ready():
  print('Bot conectado a Discord')
  
@client.event
async def on_message(message):
  if message.content.startswith('!hello'):
    await message.channel.send('Holi')

  if message.content.startswith('!sumar'):
    numeros = message.content.split()[1:]
    resultado = sum([float(num) for num in numeros])
    await message.channel.send(f'El resultado de la suma es: {resultado}')

  if message.content.startswith('!download'):
    url = message.content.split(' ')[1]
    youtube = pytube.YouTube(url)
    stream = youtube.streams.get_highest_resolution()
    filename = stream.download()
    await message.channel.send(f'Vídeo descargado como: {filename}')
    os.system(f'start {filename}')

  if message.content.startswith("!AI"):
    prompt = message.content
    response = openai.Completion.create(engine = "text-davinci-003", prompt = prompt, max_tokens = 2048)
    answer = response.choices[0].text
    await message.channel.send(answer)
    
client.run(TOKEN)