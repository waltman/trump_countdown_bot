import discord
import time

def load_dotenv():
    dotenv = dict()
    with open('.env') as f:
        for line in f:
            line = line.rstrip()
            k,v = line.split('=')
            dotenv[k] = v
    return dotenv

def decode_duration(secs):
    days = secs // 86400;  secs -= days * 86400
    hrs  = secs // 3600;   secs -= hrs  * 3600
    mins = secs // 60
    secs = secs % 60

    return days, hrs, mins, secs

def countdown():
    inaug_epoch = int(time.mktime(time.strptime("2021-01-20 12:00", "%Y-%m-%d %H:%M")))
    delta_secs = int(inaug_epoch - time.time())

    days, hrs, mins, secs = decode_duration(delta_secs)

    day_s = "day"    if days == 1 else "days"
    hr_s  = "hour"   if hrs  == 1 else "hours"
    min_s = "minute" if mins == 1 else "minutes"
    sec_s = "second" if secs == 1 else "seconds"

    return f'{days} {day_s}, {hrs} {hr_s}, {mins} {min_s}, and {secs} {sec_s}.'

dotenv = load_dotenv()
TOKEN = dotenv['DISCORD_TOKEN']

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content == 'countdown':
        msg = countdown()
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
client.run(TOKEN)
