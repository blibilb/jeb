import re
import asyncio
import datetime
import os
from discord.ext import tasks
from discord.ext import commands
from discord.ext.commands import Bot
import time
from time import sleep
from discord.utils import get
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
client = commands.Bot(command_prefix= prfx, intents=intents)

channellist = [738868024706072607, 738868024706072607,738868024706072607,622256628716273665, 510642949101584393, 733361891946266664]
medialist = [738868024706072607]

v = ['a', 'e', 'i', 'o', 'u']
c = [
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s",
    "t", "v", "w", "x", "y", "z"
]
article = ['a', 'an', 'the']

p1=['e','a','i','o','n','r','t','l','s','u']
p2=['d','g']
p3=['b','c','m','p']
p4=['f','h','v','w','y']
p5='k'
p8=['j','x']
p10=['q','z']

'''gr={}
br={}
def rep(f,d):
  with open(f,'r') as g:
    g=g.readlines()
    for i in g:
      i=i.lower()
      i=i[:-1:]
      pp=0
      for j in i:
        if j in p1:
          pp+=1
        if j in p2:
          pp+=2
        if j in p3:
          pp+=3
        if j in p4:
          pp+=4
        if j in p5:
          pp+=5
        if j in p8:
          pp+=8
        if j in p10:
          pp+=10
      d[i]=pp
    print(d)
rep('goodwords.txt',gr)
rep('badwords.txt',br)
with open('goodwords1.txt','r') as g1:
      d=json.load(g1)
      with open('goodwords1.txt','w') as g1:
        json.dump(gr,g1)
with open('badwords1.txt','r') as g1:
      d=json.load(g1)
      with open('badwords1.txt','w') as g1:
        json.dump(br,g1)'''


@client.command()
async def doom(ctx, member:discord.Member):
  role = discord.utils.get(ctx.guild.roles, name='Doomed Faggotries')
  council = discord.utils.get(ctx.guild.roles, name='Council')
  mod = discord.utils.get(ctx.guild.roles, name='Moderator')
  lean = discord.utils.get(ctx.guild.roles, name='Lean Deputy')
  admin = discord.utils.get(ctx.guild.roles, name= 'Admin')
  memer = discord.utils.get(ctx.guild.roles, name='Memer')
  if council in ctx.message.author.roles or admin in ctx.message.author.roles or mod in ctx.message.author.roles or lean in ctx.message.author.roles:
   
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
  mod = discord.utils.get(ctx.guild.roles, name='Moderator')
  lean = discord.utils.get(ctx.guild.roles, name='Lean Deputy')
  admin = discord.utils.get(ctx.guild.roles, name= 'Admin')
  memer = discord.utils.get(ctx.guild.roles, name='Memer')
  if council in ctx.message.author.roles or admin in ctx.message.author.roles or mod in ctx.message.author.roles or lean in ctx.message.author.roles:
   
   await member.remove_roles(role)
   await member.add_roles(memer)
   await ctx.send("dont be a bad boy")
  else:
   await ctx.send('u cant do that')
  await ctx.message.delete()  
  
@client.command()
async def nugget(ctx):
  await ctx.send("https://media.discordapp.net/attachments/908290444813811732/994019622930096138/tumblr_7387473ccf7467f90a5b6f8479678220_a0e2891d_540.gif")

  
@client.command()
async def slug(ctx):
  await ctx.send("https://media.discordapp.net/attachments/738868024706072607/989558602777894922/45CD5503-4AA0-4905-AB2A-2E269F4BA3B2.jpg?width=622&height=452")


@client.command()
async def ping(ctx):
    await ctx.send(client.latency)




  
@client.command()
async def names(ctx):
  nlist = 'nlist.json'
  with open(nlist, 'r') as f:
    dics = json.load(f)
    lo = ""
    for i in dics:
      lo += i + ":" + dics[i] + "\n"
    await ctx.send("```" + lo + "```")
@client.command()
async def haram(ctx):
  f=open('NO!!.txt', 'a')
  f.write(ctx.message.content[8::])
  await ctx.send('so haram')
  f.close()
@client.command()
async def haramlist(ctx):
  f=open('NO!!.txt','r')
  no=str(f.read().split())
  no=no.replace('[', '').replace(']', '').replace("'", "")
  await ctx.send("```"+no+"```")
  f.close()
  

@client.command()
async def dmr(ctx, member: discord.Member=None):
  if member==None:
    member = ctx.author
  channel = await member.create_dm()
  await ctx.message.delete()
  while True:
    try:
        sent=await ctx.send('message:')
        msg=await client.wait_for(
          'message',
          timeout=60,
          check=lambda message: message.author==ctx.author
                       and message.channel == ctx.channel
        )
        if msg:
          await sent.delete()
          await msg.delete()
          await channel.send(msg.content)
    except asyncio.TimeoutError:
      await sent.delete()
    try:
      sent=await ctx.send('continue? (n for no)')
      mg=await client.wait_for(
      'message',
      timeout=60,
      check=lambda message: message.author==ctx.author
                   and message.channel == ctx.channel
      )
      if mg.content.lower()=='n':
        await sent.delete()
        break
    except asyncio.Timeouterror: 
        await sent.delete()
        break

@client.command()
async def dm(ctx, member: discord.User=None, *, cont=None):
  if member==None:
    member = ctx.author
  channel = await member.create_dm()
  await ctx.message.delete()
  try:
    if cont==None:
      sent=await ctx.send('what do i say')
      msg=await client.wait_for(
        'message',
        timeout=60,
        check=lambda message: message.author==ctx.author
                              and message.channel == ctx.channel
      )
      if msg:
        await sent.delete()
        await msg.delete()
        await member.send(msg.content)
    else:
      await member.send(cont)
  except asyncio.TimeoutError:
    await sent.delete()

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
async def ar(ctx, users: commands.Greedy[discord.Member], *, role: discord.Role):
  council = discord.utils.get(ctx.guild.roles, name='Council')
  mod = discord.utils.get(ctx.guild.roles, name='Moderator')
  lean = discord.utils.get(ctx.guild.roles, name='Lean Deputy')
  admin = discord.utils.get(ctx.guild.roles, name= 'Admin')
  if council in ctx.message.author.roles or admin in ctx.message.author.roles or mod in ctx.message.author.roles or lean in ctx.message.author.roles:
    for user in users:
      await user.add_roles(role)
    await ctx.message.delete()
    await ctx.send('k')
  else:
    await ctx.send('u cant do that')

@client.command()
async def rr(ctx, users: commands.Greedy[discord.Member], *, role: discord.Role):
  council = discord.utils.get(ctx.guild.roles, name='Council')
  mod = discord.utils.get(ctx.guild.roles, name='Moderator')
  lean = discord.utils.get(ctx.guild.roles, name='Lean Deputy')
  admin = discord.utils.get(ctx.guild.roles, name= 'Admin')
  if council in ctx.message.author.roles or admin in ctx.message.author.roles or mod in ctx.message.author.roles or lean in ctx.message.author.roles:
    for user in users:
      await user.remove_roles(role)
    await ctx.message.delete()
    await ctx.send('k')
  else:
    await ctx.send('u cant do that')
  
@client.command()
async def taglist(ctx):
  with open('tags.txt', 'r') as t:
    t=json.load(t)
  lo=""
  for i in t.keys():
    lo += i+'\n'
  await ctx.send("```" + lo + "```")
  
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
  start = datetime.datetime(2021, random.randint(1,12), random.randint(1,28))
  end = datetime.datetime(2022, random.randint(1,5), random.randint(1,28))
  timez = end - start
  dayz = timez.days
  randays = random.randrange(dayz)
  randas=randays+1
  randate = start + datetime.timedelta(days=randays)
  randase = start + datetime.timedelta(days=randas)
  print(randate, randase)
  messag=ctx.message.content[7::]
  if messag=='':
        channel = client.get_channel(random.choice(channellist))
        messages = await channel.history(around=randate).flatten()
        rand = random.choice(messages)
        rond = random.choice(messages)
        if ctx.message.channel !=client.get_channel(ctx.guild.system_channel.id):
          return
        if 'why' in ctx.message.content.lower():
          await ctx.reply('why not', mention_author=True)
        if rand.content == "":
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
        h = random.randint(4,6)
        if h == 4:
            await asyncio.sleep(2)
            await ctx.channel.trigger_typing()
            await asyncio.sleep(len(rand.content)*0.2)
            await ctx.channel.send(rand.content)
            return
        if h==5:
            await asyncio.sleep(3)
            await ctx.channel.trigger_typing()
            await asyncio.sleep(len(rand.content)*0.2)
            await ctx.channel.send(rand.content)
            await ctx.channel.trigger_typing()
            await asyncio.sleep(len(rond.content)*0.2)
            await ctx.channel.send(rond.content)
            return
            
        else:
                thing = rand.content + " " + rond.content.lower()
                b = []
                for pos, char in enumerate(thing):
                    if (char == " "):
                        b.append(pos)
                thong = random.choice(b)
                await ctx.channel.trigger_typing()
                await asyncio.sleep(len(thing[0:thong] + dics[str(ctx.message.author)] +thing[thong::])*0.2)
                await ctx.channel.send(thing[0:thong]+thing[thong::])
  r = requests.post(
          "https://api.deepai.org/api/text-generator",
          data={
                'text': messag,
            },
          headers={'api-key': '32225aa3-a321-4c22-9145-6c43667a58f9'})
  
  t = (r.json())['output']
  print(t)
  if t == '':
       await ctx.reply('idk')

  else:
    await ctx.message.reply(t, mention_author=True)

@client.command()
async def laugh(ctx):
  laugh=['LMAO', 'lol', 'LOL', 'HAHAHA', 'lmao']
  await ctx.send(random.choice(laugh))
  await ctx.message.delete()

pchans=[920897145723301938,452978347077533707,770668464867770398]
@client.command()
async def porn(ctx):
  print(ctx.message.channel.id)
  if ctx.message.channel.id in pchans:
    await ctx.send("just search google ya horny fuck")
  else:
    await ctx.send("there's channels for that")
@client.command(aliases=['t', 'ta'])
async def tag(ctx, txt:str, *after):
  await ctx.message.delete()
  with open('tags.txt', 'r') as tags:
    tags=json.load(tags)
    if txt in tags.keys():
      await ctx.send(str(random.choice(tags[txt])))
    else:
      await ctx.send(f'{txt} doesnt exist, say "jb addtag {txt}" to add it')
@client.command()
async def addtag(ctx, tag:str=None, *, txt:str=None):
  await ctx.message.delete()
  if tag is None:
    await ctx.send("input the tags name\n` jb addtag <tag_name> <--this one <tag_content>`")
    return
  if txt is None:
    await ctx.send("input something for the tag to contain\n`jb addtag <tag_name> <tag_content> <--this one`")
    return
  with open('tags.txt', 'r') as tags:
    tags=json.load(tags)
  if tag not in tags:
    txt=[txt]
    tags[tag]=list()
    tags[tag].extend(txt)

  else:
    tags[tag].extend([txt])
  with open('tags.txt', 'w') as tag:
      json.dump(tags, tag)
  await ctx.send('saved')
@client.command() 
async def rtag(ctx, txt:str, *after):
    with open('tags.txt', 'r') as tags:
      tags=json.load(tags)
    if txt in tags.keys():
      del tags[txt]
      with open ('tags.txt','w') as tas:
        json.dump(tags, tas)
      await ctx.send(f'removed {txt}')
    else:
      await ctx.send(f"{txt} doesn't exist")
@client.command()
async def halal(ctx):
  f=open('NO!!.txt', 'r')
  g=f.read()
  g=g.replace(ctx.message.content[8::], '')
  f.close()
  f=open('NO!!.txt', 'w')
  f.write(g)
  await ctx.send('halal')
  f.close()
@client.command()
async def ip(ctx, member: discord.Member=None):
    if member==None:
      member=ctx.author
    id=str(member.id)
    with open('ip.txt', 'r') as f:
      d = json.load(f)
      if id in d.keys():
        ipp=str(member).replace(str(member)[str(member).index('#')::], '')+"'s ip is ```"+d[id]+"```"
        await ctx.send(ipp)
      else:
        
        ip= str(random.randint(1, 255))+'.'+str(random.randint(1, 255))+'.'+str(random.randint(1, 255))+'.'+str(random.randint(1, 255))
        d[id]=ip
        with open('ip.txt', 'w') as f:
                json.dump(d, f)
        ipp=str(member).replace(str(member)[str(member).index('#')::], '')+"'s ip is ```"+str(ip)+"```"
        await ctx.send(ipp)

@client.event
async def on_message(msg):
        id=str(msg.author)
        with open('goodwords1.txt','r') as g:
          g=json.load(g)
        with open('badwords1.txt','r') as b:
          b=json.load(b)
        with open('credit.txt','r') as f:
          d=json.load(f)
          if id in d.keys():
            for i in g:
              if i in msg.content.lower():
                d[id]+=g[i]
            for i in b:
              if i in msg.content.lower():
                d[id]-=b[i]
            with open('credit.txt','w') as f1:
              json.dump(d,f1)
          else:
            d[id]=0
            for i in g:
              if i in msg.content.lower():
                d[id]+=g[i]
            for i in b:
              if i in msg.content.lower():
                d[id]-=b[i]
            with open('credit.txt','w') as f1:
              json.dump(d,f1)
        if msg.author == client.user:
          return
        with open('tags.txt','r') as tags:
          tigs=json.load(tags)
          tags=tigs.keys()
          l=""
          for i in tags:
            if msg.content==i:
              l=random.choice(tigs[i])
              await msg.channel.send(l)
            
          
        if 'jb' or 'my name is' in msg.content.lower():
          await client.process_commands(msg)
          
        if isinstance(msg.channel, discord.channel.DMChannel):
          fchannels=[992818817451442246, 862462623923830876]
          for i in fchannels:
            ch=client.get_channel(i)
            await ch.send('('+str(msg.author.id)+') '+str(msg.author)+' says: '+msg.content)
        with open('NO!!.txt', 'r') as f:
          if 'halal' in msg.content or 'haram' in msg.content:
            await client.process_commands(msg)
            return
          no = f.read().split()
          k=0
          for i in no:
            if i in msg.content:
              k+=1
          if k>0:
            await msg.reply('no', mention_author=True)
        h = random.randint(1, 8)

            
          
        start = datetime.datetime(2021, random.randint(1,12), random.randint(1,28))
        end = datetime.datetime(2022, random.randint(1,5), random.randint(1,28))
        timez = end - start
        dayz = timez.days
        randays = random.randrange(dayz)
        randas=randays+1
        randate = start + datetime.timedelta(days=randays)
        randase = start + datetime.timedelta(days=randas)
        print(randate, randase)
        if client.user.mentioned_in(msg):
          if f'<@{client.user.id}' in msg.content or f'<@!{client.user.id}>' in msg.content:
            channel = client.get_channel(random.choice(medialist))
            
            messages = [message async for message in channel.history(around=randate)]
          
            message_attachments = [
            message.attachments for message in messages if message.attachments
          ]
            message_attachments = [
message.attachments for message in messages if message.attachments
        ]
            image_attachments = [
            attachment.url for attachments in message_attachments
            for attachment in attachments
          ]
            if len(image_attachments) > 0:
              random_number = random.randint(0, len(image_attachments))
              await asyncio.sleep(random.randint(1,2))
              try:
                await msg.reply(image_attachments[random_number],
                            mention_author=True)
            
              except:
                print(messages)
                rand = random.choice(messages)
                await msg.channel.send(rand.content)
          else:
            channel = client.get_channel(random.choice(channellist))
            messages = await channel.history(around=randate).flatten()
            rand = random.choice(messages)
            await msg.channel.trigger_typing()
            await asyncio.sleep(len(rand.content)*0.2)
            await msg.reply(rand.content)
        channel = client.get_channel(random.choice(channellist))
        messages = await channel.history(around=randate).flatten()
        rand = random.choice(messages)
        rond = random.choice(messages)
        if msg.channel !=client.get_channel(738868024706072607):
          return
        if 'why' in msg.content.lower():
          await msg.channel.send('why not')
        if rand.content == "":
            return
        if 'https://' in rand.content or 'https://' in rond.content:
          return
        if 'https://twitter.com' in rand.content or 'https://twitter.com' in rond.content:
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
        h = random.randint(1, 8)
        if h == 1 or h == 2 or h==3 or h==6 or h==7:
            return
        if h == 4:
            await asyncio.sleep(2)
            await msg.channel.trigger_typing()
            await asyncio.sleep(len(rand.content)*0.2)
            await msg.channel.send(rand.content)
            return
        if h==5:
            await asyncio.sleep(3)
            await msg.channel.trigger_typing()
            await asyncio.sleep(len(rand.content)*0.2)
            await msg.channel.send(rand.content)
            await msg.channel.trigger_typing()
            await asyncio.sleep(len(rond.content)*0.2)
            await msg.channel.send(rond.content)
            return
            
        else:
            
                thing = rand.content + " " + rond.content.lower()
                b = []
                for pos, char in enumerate(thing):
                    if (char == " "):
                        b.append(pos)
                thong = random.choice(b)
                await msg.channel.trigger_typing()
                await asyncio.sleep(len(thing[0:thong]+thing[thong::])*0.2)
                await msg.channel.send(thing[0:thong]+thing[thong::])

@client.event 
async def on_member_update(be,af):
  n=af.nick
  print(str(af))
  channel = await af.create_dm()
  if af.nick!=be.nick:
    for i in range(20):
      try:
        await channel.trigger_typing()
        await asyncio.sleep(random.randint(1,10))
        await channel.send('haha your name is '+n)
      except discord.Forbidden:
        await af.ban()


@client.event
async def on_member_join(member: discord.Member):
  ad = open('adjective.txt', 'r')
  an = open('animal.txt', 'r')
  anp = open('animal part.txt', 'r')
  ad1 = ad.read().split()
  an1 = an.read().split()
  anp1 = anp.read().split()
  ad.close()
  an.close()
  anp.close()
  await asyncio.sleep(2)
  sent = await member.guild.system_channel.send("```what should i name this guy```")
  try:
      
      msg = await client.wait_for(
          "message",
          timeout=60,
          check=lambda message: message.author != client.user                                  and message.channel == member.guild.system_channel 
      )
      if msg:
        if msg.content=="":
          return
        await sent.delete()
        await member.guild.system_channel.send(str("```"+msg.content+"```"))
        await member.edit(nick=str(msg.content))
        await msg.delete()

  except asyncio.TimeoutError:
    await sent.delete()
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
