import re
import os
from discord.ext import commands
import time
import json
import random
import requests
import discord
from keep_alive import keep_alive
token = os.environ['TOKEN']

client = discord.Client()

channellist = [738868024706072607, 663162356783906831]
medialist = [738868024706072607, 663162356783906831]

v=['a','e','i','o','u']
c=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
article=['a', 'an', 'the']

@client.event
async def on_message(msg):
  if msg.author==client.user:
    return
  if 'my name is' in msg.content.lower():
    name = msg.content[msg.content.lower().index('is')+1::]
    neem = str(msg.author)
    nlist= 'nlist.json'
    if os.path.exists(nlist):
      with open(nlist, 'r') as f:
        dics = json.load(f)
        if neem in dics.keys() and name == dics[neem]:
          await msg.reply("sup" + dics[neem], mention_author=True)
        if neem in dics.keys() and name != dics[neem]:
          await msg.reply("no you are" + dics[neem],
                                    mention_author=True)
        if name in dics.values() and neem not in dics.keys():
          await msg.reply("someone already took that name, " + name+"#2",mention_author=True)

    if neem not in dics.keys() and name not in dics.values():
      dics[neem] = name
      with open(nlist, 'w') as f:
        json.dump(dics, f)
        await msg.reply("hello i will never forget you," + name,
                        mention_author=True)
  if msg.content.lower().startswith('jb'):
    if "names" in msg.content.lower():
      nlist= 'nlist.json'
      with open(nlist, 'r') as f:
        dics = json.load(f)
        for k in dics.keys():
          await msg.channel.send(k + ': ' + str(dics[k]))
        return
          
          
      
    #temporary generator 
    r = requests.post("https://api.deepai.org/api/text-generator", data={'text': msg.content[3::],},headers={'api-key': '32225aa3-a321-4c22-9145-6c43667a58f9'})
    t = (r.json())['output']
    tt = t.replace("\n\n", " ")
    t2 = tt.replace("\ ", "")
    ttt = t2.replace("}", "")
    t4 = ttt.partition(".")
    t5 = t4[random.randint(0,1)]
    if '"' in t5:
      t5 = '"' + t5
    t5=t5+'.'
    v=['a','e','i','o','u']
    c=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
    if msg.content.endswith("?"):
      await msg.reply(t5, mention_author=True)
      return
    if msg.content[3:4] in v:
      if msg.content[3:5].lower()=="an":
        await msg.reply(t5, mention_author=True)
      else:
        await msg.reply("An"+" "+t5, mention_author=True)
    if msg.content[3:4] in c:
      if msg.content[3:6].lower()=="the":
        await msg.reply(t5, mention_author=True)
      else:
        await msg.reply("The"+" "+t5, mention_author=True)
    
    else:
      await msg.reply(t5, mention_author=True)
    print(t5)
  if client.user.mentioned_in(msg):
    channel = client.get_channel(random.choice(medialist))
    messages = [message async for message in channel.history(limit=3500)]
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
    else:
      rand = random.choice(messages)
      await msg.channel.send(rand.content)
  else:
    channel = client.get_channel(random.choice(channellist))
    messages = await channel.history(limit=3500).flatten()
    rand = random.choice(messages)
    rond=random.choice(messages)
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
    nlist= 'nlist.json'
    with open(nlist, 'r') as f:
      dics = json.load(f)
      namel=list(dics.keys())
    h = random.randint(1,5)
    if h==1 or h==2 or h==3 or h==4:
      await msg.channel.send(rand.content)
      await msg.channel.send(rond.content)
    else:
      if str(msg.author) in namel:
        thing=rand.content+" "+rond.content.lower()
        b=[]
        for pos,char in enumerate(thing):
          if(char == " "):
            b.append(pos)
        thong = random.choice(b) 
        await msg.channel.send(thing[0:thong]+dics[str(msg.author)]+thing[thong::]) 

@client.event
async def on_ready():
    print('{0.user} ready farts'.format(client))
keep_alive()
client.run(token)
