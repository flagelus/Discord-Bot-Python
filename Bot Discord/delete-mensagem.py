import discord
client = discord.Client()


@client.event
async def on_message(message):
    if str(message.channel) == "imagem" and message.content != "":
        await message.channel.purge(limit=1)

client.run('OTM2MzMzMjU4MTcyNTUxMjA5.YfLqTA.ELRnQSqYjQMeSayP1SOwCkIDRfo')
