import discord
import os
import time
from chomsky import chomsky
from well_actually import well_actually

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

def countdown(inaug_epoch):
    delta_secs = int(inaug_epoch - time.time())
    if delta_secs < 0:
        sign = "-"
        delta_secs = -delta_secs
    else:
        sign = ""

    days, hrs, mins, secs = decode_duration(delta_secs)

    day_s = "day"    if days == 1 else "days"
    hr_s  = "hour"   if hrs  == 1 else "hours"
    min_s = "minute" if mins == 1 else "minutes"
    sec_s = "second" if secs == 1 else "seconds"

    return f'{sign}{days} {day_s}, {hrs} {hr_s}, {mins} {min_s}, and {secs} {sec_s}.'

def swatch():
    return f'@{((int(time.time()) + 3600) % 86400) // 86.4 :03.0f}'

def conspiracy():
    with os.popen('/home/waltman/bin/conspiracy_theory') as f:
        return f.read()

dotenv = load_dotenv()
TOKEN = dotenv['DISCORD_TOKEN']
inaug_epoch = int(time.mktime(time.strptime("2021-01-20 12:00", "%Y-%m-%d %H:%M")))
inaug_epoch_2025 = int(time.mktime(time.strptime("2025-01-20 12:00", "%Y-%m-%d %H:%M")))

vaccine_jab1 = int(time.mktime(time.strptime("2021-04-15 13:30", "%Y-%m-%d %H:%M")))
vaccine_jab1_week = int(time.mktime(time.strptime("2021-04-29 13:30", "%Y-%m-%d %H:%M")))
vaccine_jab2 = int(time.mktime(time.strptime("2021-05-06 13:30", "%Y-%m-%d %H:%M")))
vaccine_jab2_week = int(time.mktime(time.strptime("2021-05-20 13:30", "%Y-%m-%d %H:%M")))
vaccine_jab3 = int(time.mktime(time.strptime("2021-11-11 13:30", "%Y-%m-%d %H:%M")))

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    content = message.content.lower()
    if content == 'countdown':
        msg = countdown(inaug_epoch_2025)
        print(f'Message from {message.author}, countdown={msg}')
        await message.channel.send(msg)
    elif content == 'swatch':
        msg = swatch()
        print(f'Message from {message.author}, swatch={msg}')
        await message.channel.send(msg)
    elif content == 'chomsky':
        msg = chomsky()
        print(f'Message from {message.author}, chomsky={msg}')
        await message.channel.send(msg)
    elif content == 'conspiracy':
        msg = conspiracy()
        print(f'Message from {message.author}, conspiracy={msg}')
        await message.channel.send(msg)
    elif content == 'well actually':
        msg = well_actually()
        print(f'Message from {message.author}, well_actually={msg}')
        await message.channel.send(msg)
    elif content == 'walt vaccine':
        m1 = countdown(vaccine_jab1)
        m2 = countdown(vaccine_jab1_week)
        m3 = countdown(vaccine_jab2)
        m4 = countdown(vaccine_jab2_week)
        m5 = countdown(vaccine_jab3)
        msg = f'**First jab:** {m1}\n**14 days after first jab:** {m2}\n**Second jab:** {m3}\n**14 days after second jab:** {m4}\n**Third jab:** {m5}'
        print(f'Message from {message.author}, walt vaccine={msg}')
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(f'{client.user} connected to Discord!')
    print('------')
    
client.run(TOKEN)
