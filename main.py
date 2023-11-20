

# invite link = https://discord.com/api/oauth2/authorize?client_id=1175904676730912921&permissions=1084479765568&scope=bot
import discord
import requests
from bs4 import BeautifulSoup


def get_stats(message):
    message = message.split(' ')
    username = message[1]

    url = "https://r6.tracker.network/profile/pc/" + username

    page = requests.get(url)
    doc = BeautifulSoup(page.text, features="html.parser")

    dirty_stats = doc.find_all(class_="trn-defstat")

    stats = []

    for i in dirty_stats:
        i = i.text
        stats.append(i)

    clean_stats = []

    for i in stats:
        i = i.split()
        if len(i) == 0:
            continue
        clean_stats.append(i)

    client_message = ""

    kd_flag = False
    rank_flag = False
    max_rank_flag = False
    matches_played_flag = False
    win_p_flag = False

    for i in clean_stats:
        if i[0] == "KD":
            if not kd_flag:
                client_message += f"K/D : {i[1]}\n"
                kd_flag = True
        elif i[0] == "Rank":
            if not rank_flag:
                client_message += f"Rank: {i[1] + ' ' + i[2]}\n"
                rank_flag = True
        elif i[0] == "Max":
            if not max_rank_flag:
                client_message += f"Max Rank: {i[2] + ' ' + i[3]}\n"
                max_rank_flag = True
        elif i[0] == "Matches":
            if not matches_played_flag:
                client_message += f"Matches Played: {i[2]}\n"
                matches_played_flag = True
        elif i[0] == 'Win':
            if not win_p_flag:
                client_message += f"Win%: {i[2]}\n"
                win_p_flag = True
    print(client_message)
    return client_message


async def send_message(message, user_message, is_private):
    try:
        response = get_stats(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    token = 'you want this dont you'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if message.author == client.user:
            return
        elif client.user.mention in user_message.split():
            await send_message(message, user_message, is_private=False)
        # elif username == "the_petite_nut":
        #     await message.channel.send("logan you're gay and likes petite femboys")
        # elif username == "legacy3393":
        #     await message.channel.send("tom likes little boys and has them poop on his chest")

        print(f'{username} said: {user_message} in {channel}')

        # if user_message[0] == "?":
        #     user_message = user_message[1::]
        #     await send_message(message, user_message, is_private=True)
        # else:
        #     await send_message(message, user_message, is_private=False)

    client.run(token)


if __name__ == '__main__':
    run_discord_bot()
