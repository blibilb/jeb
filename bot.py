import re
import asyncio
import datetime
import os
from discord.ext import tasks
from discord.ext import commands
from discord.ext.commands import Bot
import time
from time import sleep
import json
import random
import requests
import discord
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
token = os.environ['TOKEN']
def permute(inp):
    n = len(inp)
    mx = 1 << n
    inp = inp.lower()
    l=[]
    for i in range(mx):
        combination = [k for k in inp]
        for j in range(n):
            if (((i >> j) & 1) == 1):
                combination[j] = inp[j].upper()
 
        temp = ""
        for i in combination:
            temp += i
        print(temp)
        l.append(temp)
    return l

permu=permute("MY ")+permute("MY")
prfx=['jb ', 'Jb ', 'JB ', 'jB ','jb', 'Jb', 'JB', 'jB']+permu
client = commands.Bot(command_prefix= commands.when_mentioned_or(prfx), intents=intents)

channellist = [
    738868024706072607, 663162356783906831, 453090899144998918,
    510642949101584393, 733361891946266664
]
medialist = [738868024706072607]

v = ['a', 'e', 'i', 'o', 'u']
c = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s",
    "t", "v", "w", "x", "y", "z"
]
article = ['a', 'an', 'the']

@client.command()
async def doom(ctx, member:discord.Member):
  role = discord.utils.get(ctx.guild.roles, name='Doomed Faggotries')
  council = discord.utils.get(ctx.guild.roles, name='Council')
  memer = discord.utils.get(ctx.guild.roles, name='Memer')
  if council in ctx.message.author.roles:
    await member.add_roles(role)
    await member.remove_roles(memer)
    await ctx.send("L")
  else:
    await ctx.send("u cant do that")
  await ctx.message.delete()

@client.command()
async def undoom(ctx, member:discord.Member):
  role = discord.utils.get(ctx.guild.roles, name='Doomed Faggotries')
  council = discord.utils.get(ctx.guild.roles, name='Council')
  memer = discord.utils.get(ctx.guild.roles, name='Memer')
  if council in ctx.message.author.roles:
   
   await member.remove_roles(role)
   await member.add_roles(memer)
   await ctx.send("dont be a bad boy")
  else:
   await ctx.send('u cant do that')
  await ctx.message.delete()  
  
@client.command()
async def nugget(ctx):
  await ctx.send("https://media.discordapp.net/attachments/913860576399200307/989552640063070268/unknown-3.png?width=1025&height=436")

  
@client.command()
async def slug(ctx):
  await ctx.send("https://media.discordapp.net/attachments/738868024706072607/989558602777894922/45CD5503-4AA0-4905-AB2A-2E269F4BA3B2.jpg?width=622&height=452")


@client.command()
async def ping(ctx):
    await ctx.send(client.latency)

@client.command()
async def ip(ctx, member: discord.Member):
    ip= str(random.randint(1, 255))+'.'+str(random.randint(1, 255))+'.'+str(random.randint(1, 255))+'.'+str(random.randint(1, 255))
      
    ipp=str(member).replace(str(member)[str(member).index('#')::], '')+"'s ip is "+str(ip)
    await ctx.send(ipp)

  
@client.command()
async def names(ctx):
  nlist = 'nlist.json'
  with open(nlist, 'r') as f:
    dics = json.load(f)
    lo = ""
    for i in dics:
      lo += i + ":" + dics[i] + "\n"
    await ctx.send("```" + lo + "```")
  await ctx.message.delete()

@client.command()
async def say(ctx):
  await ctx.message.delete()
  try:
    if ctx.message.content[7::]=='':
      sent = await ctx.send('say what')
      msg = await client.wait_for(
          "message",
          timeout=60,
          check=lambda message: message.author == ctx.author
                                and message.channel == ctx.channel
      )
      if msg:
        await sent.delete()
        await msg.delete()
        await ctx.send(msg.content)
    else:
        await ctx.send(ctx.message.content[7::])
  except asyncio.TimeoutError:
    await sent.delete()
snipe_message_author={}
snipe_message_content={}
@client.event
async def on_message_delete(message):
  snipe_message_author[message.channel.id] = message.author
  snipe_message_content[message.channel.id]= message.content
  await sleep(60)
  del snipe_message_author[message.channel.id]
  del snipe_message_content[message.channel.id]
  
@client.command()
async def snipe(ctx):
  channel = ctx.channel
  try:
    snipeEmbed = discord.Embed(title=f"last deleted message in #{channel.name}", description = snipe_message_content[channel.id])
    snipeEmbed.set_footer(text=f"deleted by {snipe_message_author[channel.id]}")
    await ctx.send(embed = snipeEmbed)
  except:
    await ctx.send('nothin')
@client.command()
async def name(ctx):
    print(ctx.message.content)
    if 'my name is' in ctx.message.content.lower():

        name = ctx.message.content[ctx.message.content.lower().index('name is') + 7::]
        neem = str(ctx.message.author)
        nlist = 'nlist.json'
        if os.path.exists(nlist):
            with open(nlist, 'r') as f:
                dics = json.load(f)
                if neem in dics.keys() and name == dics[neem]:
                    await ctx.message.reply("sup" + dics[neem], mention_author=True)
                if neem in dics.keys() and name != dics[neem]:
                    await ctx.message.reply("no you are" + dics[neem],
                                    mention_author=True)
                if name in dics.values() and neem not in dics.keys():
                    await ctx.message.reply("someone already took that name, " + name +
                                    "#2",
                                    mention_author=True)

        if neem not in dics.keys() and name not in dics.values():
            dics[neem] = name
            with open(nlist, 'w') as f:
                json.dump(dics, f)
                await ctx.message.reply("hello i will never forget you," + name,
                                mention_author=True)
        return

@client.command()
async def gen(ctx):
  messag=ctx.message.content[7::]
  r = requests.post(
          "https://api.deepai.org/api/text-generator",
          data={
                'text': messag,
            },
          headers={'api-key': '32225aa3-a321-4c22-9145-6c43667a58f9'})
  t = (r.json())['output']
  tt = t.replace("\n\n", " ")
  t2 = tt.replace("\ ", "")
  ttt = t2.replace("}", "")
  t4 = ttt.partition(".")
  t5 = t4[random.randint(0, 1)]
  if '"' in t5:
      t5 = '"' + t5
  t5 = t5 + '.'
  v = ['a', 'e', 'i', 'o', 'u']
  c = [
            "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q",
            "r", "s", "t", "v", "w", "x", "y", "z"
        ]
  if messag.endswith("?"):
      await ctx.message.reply(t5, mention_author=True)
      return
  if messag[0] in v:
    if messag[0:1].lower() == "an":
      await ctx.message.reply(t5, mention_author=True)
    else:
      if t5 == '..':
        ins = requests.get("https://insult.mattbas.org/api/insult")
        t5 = ins.text
        if 'as an' in t5:
          t5 = 'You are an ' + t5[t5.index('as an') + 5::]
        if 'as a ' in t5:
          t5 = 'You are a ' + t5[t5.index('as a ') + 5::]
        await ctx.message.reply(t5, mention_author=True)
      else:
        await ctx.message.reply("An" + " " + t5, mention_author=True)
      return

  if messag[0] in c:
    if messag[0:3].lower() == "the":
      await ctx.message.reply(t5, mention_author=True)
    else:
      if t5 == '..':
        ins = requests.get("https://insult.mattbas.org/api/insult")
        t5 = ins.text
        if 'as an' in t5:
          t5 = 'You are an ' + t5[t5.index('as an') + 6::]
        if 'as a ' in t5:
          t5 = 'You are a ' + t5[t5.index('as a ') + 5::]
        await ctx.message.reply(t5, mention_author=True)
      else:
        await ctx.message.reply("The" + " " + t5, mention_author=True)
      return

@client.event
async def on_message(msg):
        if msg.author == client.user:
          return
        start = datetime.datetime(2020, random.randint(1,12), random.randint(1,28))
        end = datetime.datetime(2022, random.randint(1,5), random.randint(1,28))
        timez = end - start
        dayz = timez.days
        randays = random.randrange(dayz)
        randas=randays+1
        randate = start + datetime.timedelta(days=randays)
        randase = start + datetime.timedelta(days=randas)
        print(randate, randase)
        if client.user.mentioned_in(msg):
          channel = client.get_channel(random.choice(medialist))
          messages = [message async for message in channel.history(around=randate)]
          message_attachments = [
            message.attachments for message in messages if message.attachments
        ]
          image_attachments = [
            attachment.url for attachments in message_attachments
            for attachment in attachments
        ]
          if len(image_attachments) > 0:
            random_number = random.randint(0, len(image_attachments))
            await msg.reply(image_attachments[random_number],
                            mention_author=True)
            return
          else:
            rand = random.choice(messages)
            await msg.channel.send(rand.content)
            return
        channel = client.get_channel(random.choice(channellist))
        messages = await channel.history(around=randate).flatten()
        rand = random.choice(messages)
        rond = random.choice(messages)
        if rand.content == "":
            return
        if "jb" in rand.content.lower():
            return
        if "jb" in rond.content.lower():
            return
        if "https://tempobot.net/premium" in rand.content:
            return
        if "https://tempobot.net/premium" in rond.content:
            return
        if rond.author == client.user:
          return
        if rand.author == client.user:
          return
        nlist = 'nlist.json'
        with open(nlist, 'r') as f:
            dics = json.load(f)
            namel = list(dics.keys())
        h = random.randint(1, 6)
        if h == 1 or h == 2 or h==3:
            return
        if h == 4:
            await msg.channel.trigger_typing()
            await asyncio.sleep(random.randint(1,10))
            await msg.channel.send(rand.content)
        if h==5:
            await msg.channel.trigger_typing()
            await asyncio.sleep(random.randint(1,10))
            await msg.channel.send(rand.content)
            await msg.channel.trigger_typing()
            await asyncio.sleep(random.randint(1,10))
            await msg.channel.send(rond.content)
        else:
            if str(msg.author) in namel:
                thing = rand.content + " " + rond.content.lower()
                b = []
                for pos, char in enumerate(thing):
                    if (char == " "):
                        b.append(pos)
                thong = random.choice(b)
                await msg.channel.send(thing[0:thong] + dics[str(msg.author)] +
                                       thing[thong::])


@client.event
async def on_member_join(member: discord.Member):
    ad = open('adjective.txt', 'r')
    an = open('animal.txt', 'r')
    anp = open('animal part.txt', 'r')
    ad1 = ad.read().split()
    an1 = an.read().split()
    anp1 = anp.read().split()
    await member.edit(nick=random.choice(ad1) + ' ' + random.choice(an1) +
                      ' ' + random.choice(anp1))
    ad.close()
    an.close()
    anp.close()

'''@tasks.loop(seconds=3600)
async def mytask():
  guid=client.get_guild(452964222867865616)
  users= guid.guild.members
  use=random.choice(users)
  ad=open('adjective.txt','r')
  an=open('animal.txt','r')
  anp=open('animal part.txt','r')
  ad1=ad.read().split()
  an1=an.read().split()
  anp1=anp.read().split()
  await use.edit(nick=random.choice(ad1)+' '+random.choice(an1)+' '+random.choice(anp1))
  ad.close()
  an.close()
  anp.close()
  print(random.choice(an1)+' '+random.choice(anp1))'''

#mytask.start()
@client.event
async def on_ready():
    print('{0.user} ready farts'.format(client))

keep_alive()
client.run(token)
