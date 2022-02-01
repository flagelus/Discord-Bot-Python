import discord

client = discord.Client()


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("opa"):

        if str(message.author) == "":
            await message.channel.send("Oi @" + str(message.author) + " sua cheirosa...")
        if str(message.author) == "Flavio#5498":
            await message.channel.send("Eai @" + str(message.author) + " meu patrão.")
        else:
            await message.channel.send("Eu sou senhor new vegas to preparando as musicas")

client.run('OTM2MzMzMjU4MTcyNTUxMjA5.YfLqTA.ELRnQSqYjQMeSayP1SOwCkIDRfo')
