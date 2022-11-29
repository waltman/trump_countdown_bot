import discord
import os
import time
from chomsky import chomsky
from well_actually import well_actually
import calendar
import datetime

def days_to_ymd(days):
    days_in_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    ]
    now = datetime.datetime.fromtimestamp(time.time())
    year = now.year
    month = now.month-1
    years = 0
    months = 0
    while (True):
        dim = days_in_month[1][month] if calendar.isleap(year) else days_in_month[0][month]
        if dim > days:
            return years, months, days
        else:
            days -= dim
            months += 1
            if months == 12:
                months = 0
                years += 1
            month -= 1
            if month < 0:
                month = 11
                year -= 1

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
    years, months, days2 = days_to_ymd(days)

    return years, months, days2, hrs, mins, secs

def countdown(inaug_epoch):
    delta_secs = int(inaug_epoch - time.time())
    if delta_secs < 0:
        sign = ""
        delta_secs = -delta_secs
    else:
        sign = "-"

    years, months, days, hrs, mins, secs = decode_duration(delta_secs)

    year_s  = "year"   if years == 1  else "years"
    month_s = "month"  if months == 1 else "months"
    day_s   = "day"    if days == 1   else "days"
    hr_s    = "hour"   if hrs  == 1   else "hours"
    min_s   = "minute" if mins == 1   else "minutes"
    sec_s   = "second" if secs == 1   else "seconds"

    return f'{sign}{years} {year_s}, {months} {month_s}, {days} {day_s}, {hrs} {hr_s}, {mins} {min_s}, and {secs} {sec_s}.'

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
vaccine_jab4 = int(time.mktime(time.strptime("2022-06-17 10:15", "%Y-%m-%d %H:%M")))
vaccine_jab5 = int(time.mktime(time.strptime("2022-10-06 13:30", "%Y-%m-%d %H:%M")))

class TrumpCountdownClient(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user)
        print(f'{self.user} connected to Discord!')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author == self.user:
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
            m6 = countdown(vaccine_jab4)
            m7 = countdown(vaccine_jab5)
            msg = f'**First jab:** {m1}\n**Second jab:** {m3}\n**First booster:** {m5}\n**Second booster:** {m6}\n**Bivalent omicron booster:** {m7}'
            print(f'Message from {message.author}, walt vaccine={msg}')
            await message.channel.send(msg)
        elif content.startswith('covid pa graph'):
            county = content.split()[-1].title()
            fname = os.path.join('/home/waltman/perl/projects/covid19/graphs', county + "_cases.png")
            if os.path.exists(fname):
                print(f'Message from {message.author}, sending {fname}')
                await message.channel.send(file=discord.File(fname))
            else:
                msg = f'Sorry, no graph for {county}'
                print(f"Message from {message.author}, {fname} doesn't exist")
                await message.channel.send(msg)

intents = discord.Intents.default()
intents.message_content = True
client = TrumpCountdownClient(intents=intents)
client.run(TOKEN)
