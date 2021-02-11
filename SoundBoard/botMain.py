import discord
import nacl as pynacl
import opus_api
import ctypes
import json
import random
import time
import os
import bot
import asyncio

void = None

#pointless line
NULLPTR = None 

TOKEN = bot.token
client = discord.Client()
loop = asyncio.get_event_loop()


# make sure of a sucessfull connection
@client.event
async def on_ready():
    print("We have loged in as {0.user}".format(client))
    return None

# the main boi (everything is controlled through message moderation so it's all in here)
@client.event
async def on_message(message):

    # make sure we aren't replying to ourselves  
    if message.author == client.user:
        return void

    # say a random crucible text quote is the word crucible is said anywhere in chat 
    #elif (message.content.find("building") != -1 or message.content.find("tf2") != -1):
        #await message.channel.send(random.choice(EngineerTF2.quotes))

    # monitor for the command character
    elif message.content.startswith('|'):
        
        #this chunk sets up the the file path of a potential sound
        path = pathCheck(message.content)

        # this checks the file path leads to a file as well as if the user is connected to a voice channel
        if path != 0:
            print("File " + path + " found")
            if message.author.voice != None or client.user.voice == None:
                    # the voice handler function handles the voice
                    print("Number of users: " + str(len(message.author.voice.channel.voice_states)) + "\nUser Limit: " + str(message.author.voice.channel.user_limit))
                    if message.author.voice.channel.user_limit > len(message.author.voice.channel.voice_states) or \
                    message.author.voice.channel.user_limit == 0:
                        await voiceHandler(path, message.author)
                    else:
                        await message.channel.send("Too many pardners in that channel pardner")
            else:
                await message.channel.send("Spy sappin the voice channel!")
        
        # the stuff that handles bringing up the help thing
        elif message.content.startswith("|help"):
            quotesReadable = {('|' + x.replace(".wav", "")) for x in bot.voiceQuotes}
            quotesPrint = ""
            for x in quotesReadable:
                quotesPrint += x + '\n'
            await message.channel.send(quotesPrint)

        # if the file path isnt a a real file    
        else:
            print("File not found")
            await message.channel.send("Sound file Not Found")
            
        
    #gotta return something or else I feel weird
    return void


async def voiceHandler(filepath, author):
    # gets a VoiceConnection(VoiceProtocall  ) object from connecting to a voice channel
    VP = await author.voice.channel.connect()

    # plays the file and checks for when it's finnished
    VP.play(discord.FFmpegOpusAudio(filepath))
    time.sleep(1)
    while VP.is_playing():
        time.sleep(1)
    await VP.disconnect()
    return void

def pathCheck(text):
    pathWav = "Sounds/" + text[1:len(text)] + ".wav"
    pathMp3 = "Sounds/" + text[1:len(text)] + ".mp3"
    if os.path.isfile(pathWav):
        return pathWav
    elif os.path.isfile(pathMp3):
        return pathMp3
    else:
        return 0


# runs the program using the super secret bot token
if TOKEN != "":
    loop.run_until_complete(client.run(TOKEN))
    
else:
    print("No bot token identified, please create token.txt in the main directory containing a discord bot token")
