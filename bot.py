import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    token = 'MTE3NTkwNDY3NjczMDkxMjkyMQ.GZjGoh.zTR4iN_nYBZZcmnVBGpJPh6tUa2ssx3cQp3gEM'
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} is running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(user_message)

        await send_message(message, user_message, is_private=False)

        # print(f"{username} said: {user_message}")
        # if user_message[0] == '?':
        #     user_message = user_message[1::]
        #     await send_message(message, user_message, is_private=True)
        # else:
        #     await send_message(message, user_message, is_private=False)

    client.run(token)

