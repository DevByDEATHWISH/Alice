import discord
import config
import alice
import response

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        async with message.channel.typing():
            user_message = f"{message.author.name}: {message.content}"
            response.input = user_message

        await message.reply(alice.get_response())

client.run(config.TOKEN)