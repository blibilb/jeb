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
channellist = [
    985005087753658378, 943080827644936232, 833275609136103494,
    834793071799435274, 845471214613037096, 843047704745345064,
    979931823901655044
]
medialist = [
    943080827644936232, 833275609136103494, 845471214613037096,
    985005087753658378
]


@client.event
async def on_message(msg):
  if msg.author==client.user:
    return
  if msg.content.lower().startswith('my name is'):
    name = msg.content[10::]
    neem = str(msg.author)
    nlist= 'nlist.json'
    if os.path.exists(nlist):
      with open(nlist, 'r') as f:
        dics = json.load(f)
        if neem in dics.keys() and name == dics[neem]:
          await msg.reply("sup" + dics[neem],
                                    mention_author=True)
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
          
          
      
    #temporary generator 
    r = requests.post("https://api.deepai.org/api/text-generator", data={'text': msg.content[3::],},headers={'api-key': '32225aa3-a321-4c22-9145-6c43667a58f9'})
    t = (r.json())['output']
    tt = t.replace("\n\n", " ")
    t2 = tt.replace("\ ", "")
    ttt = t2.replace("}", "")
    t4 = ttt.partition(".")
    t5 = t4[0]
    if '"' in t5:
      t5 = '"' + t5
      await msg.reply(t5, mention_author=True)
      print(t5)
  if client.user.mentioned_in(msg):
    channel = client.get_channel(random.choice(medialist))
    messages = [message async for message in channel.history(limit=None)]
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
    messages = await channel.history(limit=None).flatten()
    rand = random.choice(messages)
    rond=random.choice(messages)
    if rand.content == "": 
      return
    if "jb" in rand.content.lower() or rond.content.lower():
      return
    if "https://tempobot.net/premium" in rand.content or rond.content:
      return
    else:
      await msg.channel.send(rand.content+" "+rond.content)

@client.event
async def on_ready():
    print('{0.user} ready farts'.format(client))


keep_alive()
client.run(token)
