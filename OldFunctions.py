HALLOWEEN_CHANNEL_ID = 0
HALLOWEEN_MESSAGES = ["This is what I am wearing this year\nhttps://i.kym-cdn.com/photos/images/original/001/185/550/6d4.jpg\nHAPPY HALLOWEEN",
                      "This is a costume from one of my fans\nhttps://i.etsystatic.com/6439119/r/il/1a516c/1293844214/il_570xN.1293844214_c0tu.jpg\nHAPPY HALLOWEEN",
                      "Boo I am a witch\nhttps://img00.deviantart.net/f7e1/i/2016/304/3/c/halloween_d_va_by_liuhao726-damu3ey.jpg\nHAPPY HALLOWEEN",
                      "I even have halloween costumes for work!\nhttps://pre00.deviantart.net/00b6/th/pre/i/2016/305/2/7/d_va__halloween_mod__by_sticklove-damyueh.png\nHAPPY HALLOWEEN",
                      "Lucio came to my party as a pirate *What a hunk of man*\nhttps://66.media.tumblr.com/1ce7ab1243017fdafc8d860098a0702f/tumblr_oxk58741Zb1u1s9r3o1_500.png\nHAPPY HALLOWEEN",
                      "Witches always need a cat meow :3\nhttps://pre00.deviantart.net/ea9b/th/pre/i/2018/284/5/8/halloween_dva_by_xishka-dcp7ipw.png\nHAPPY HALLOWEEN",
                      "Are fairies allowed to join in with halloween?\nhttps://cdn.shopify.com/s/files/1/0808/7195/products/Reservation_Overwatch_D.VA_Magical_Girl_Cosplay_Dress_CP179465_large.jpg?v=1515031826\nHAPPY HALLOWEEN",
                      "This one is one of my scariest it even freaked me out\nhttps://i1.wp.com/pm1.narvii.com/6599/8f40f9e8441b4aa9273d179793ffd1efaf98c251_hq.jpg?resize=600%2C633&ssl=1\nHAPPY HALLOWEEN",
                      "Pumpkins are my favourite part of halloween\nhttps://orig00.deviantart.net/b10a/f/2016/300/7/4/pumpkin_dva_by_madsmadnessrage-damfrqd.png\nHAPPY HALLOWEEN",
                      "Mercy decided to borrow a mech so she could look like me\nhttps://ae01.alicdn.com/kf/HTB1OfVDNXXXXXXbaXXXq6xXFXXXH/D-VA-skin-concept-Costume-3D-Print-Mercy-D-Va-Suit-Halloween-Dva-Cosplay-Costumes.jpg_640x640.jpg\nHAPPY HALLOWEEN",
                      "Spooky Scary Skeletons tee hee\nhttps://i.pinimg.com/originals/49/5f/38/495f38cf567a979af59ac84455576450.jpg\nHAPPY HALLOWEEN",
                      "D.Va can't have all the fun\nHappy Birthday @Jess\nhttps://66.media.tumblr.com/7bb0d95cb3b26a43c109005d226c7d5d/tumblr_otw6p310w91vuigsoo1_1280.png",
                      "Mei once held a halloween party and its was chilly brrrrr\nhttps://pre00.deviantart.net/9407/th/pre/i/2016/341/f/d/d_va___overwatch_by_sciamano240-daqu8q2.jpg\nHAPPY HALLOWEEN",
                      "Remember when I pranked everyone that I had died LMAO\nhttps://i.kym-cdn.com/photos/images/original/001/179/642/20e.png\nHAPPY HALLOWEEN",
                      "Jess I heard you went as me for halloween but that isn't very spooky\nhttps://media.discordapp.net/attachments/471079094365323286/505823884516261890/20181027_200934.jpg?width=613&height=818\nHAPPY HALLOWEEN",
                      "I went as a witch again :P\nhttps://i.kym-cdn.com/photos/images/original/001/188/287/d1a.jpg\nHAPPY HALLOWEEN"]
HALLOWEEN_MESSAGES_COUNTER = 0

# Search for a new latest spheal and post if it is new
async def halloweenTime():
    await client.wait_until_ready()
    global HALLOWEEN_CHANNEL_ID
    global HALLOWEEN_MESSAGES
    global HALLOWEEN_MESSAGES_COUNTER
    while not client.is_closed():
        halloween = datetime.date(2018, 10, 31) # TODO: CHANGE THIS TO HALLOWEEN
        today = datetime.datetime.today()
        if halloween.day == today.day and halloween.month == today.month:
            if HALLOWEEN_CHANNEL_ID == 0:
                halloweenChannel = await client.get_guild(GAMESOC_GUILD_ID).create_text_channel('happy-halloween')
                HALLOWEEN_CHANNEL_ID = halloweenChannel.id
                everyone = client.get_guild(GAMESOC_GUILD_ID).default_role
                await halloweenChannel.set_permissions(everyone, read_messages=True, send_messages=False)
                await halloweenChannel.send("Hiya my name is Hana Song (송하나) otherwise known as D.Va and I love halloween :3")
                await halloweenChannel.send("Long story short, I heard Jess looooooves halloween as much as me so I asked Sombra to hack into this bot so I can share some of my cool halloween costumes :P")
                await halloweenChannel.send("So yeah here we go!! I am so excited")
                await halloweenChannel.send("- Love D.Va")
                await halloweenChannel.send("https://www.youtube.com/watch?v=PXZmfdSm7t0")
            else:
                halloweenChannel = client.get_channel(HALLOWEEN_CHANNEL_ID)
                if HALLOWEEN_MESSAGES_COUNTER < len(HALLOWEEN_MESSAGES):
                    await halloweenChannel.send(HALLOWEEN_MESSAGES[HALLOWEEN_MESSAGES_COUNTER])
                    HALLOWEEN_MESSAGES_COUNTER = HALLOWEEN_MESSAGES_COUNTER + 1
        await asyncio.sleep(5000)
        # task runs every 3*60*60/2 seconds (1 and 1/2 hours) (16 messages over 24 hour period) (slightly less)

@client.event
async def on_member_join(member):
    # Special announcement for member 500
    gameSocServer = client.get_guild(GAMESOC_GUILD_ID)
    if len(gameSocServer.members) == 501:
        gameSocGeneralChannel = client.get_channel(GAMESOC_GENERAL_CHANNEL_ID)
        await gameSocGeneralChannel.send("🎺🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎺")
        await gameSocGeneralChannel.send("**Congratulations %s, you are our 500th member of the server, you win nothing**" % member.display_name)
        await gameSocGeneralChannel.send("🎺🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎺")
        await gameSocGeneralChannel.send("https://www.youtube.com/watch?v=-YCN-a0NsNk")

# If an egm is mentioned increment counter and then respond to the message
# This isn't perfect as there are some words that contain egm but so be it does it matter
# Here is the list: https://www.wordfind.com/contains/Egm/

# FUN IS OVER EGM EASTER EGG IS DONE
elif "EGM" in message.content.upper():
    counterChannel = client.get_channel(EGM_COUNTER_CHANNEL_ID)
    counterMessage = await counterChannel.get_message(EGM_COUNTER_MESSAGE_ID)
    egmCounter = int(counterMessage.content)
    egmCounter += 1
    await message.channel.send("Current EGM counter is at %s this year" % egmCounter)
    await counterMessage.edit(content = egmCounter)

    # Testing getting days since
    dayMessage = await counterChannel.get_message(EGM_DAYS_MESSAGE_ID)
    pastDay = datetime.datetime.strptime(dayMessage.content, '%Y-%m-%d')
    today = datetime.datetime.today()
    await message.channel.send("Days since last call for an EGM: %s" % (today - pastDay).days)
    await dayMessage.edit(content = datetime.date.today())

# Reset counter command for EGM
if message.content.upper() == "EGM?RESET" and message.channel.id == EGM_COUNTER_CHANNEL_ID:
    counterChannel = client.get_channel(EGM_COUNTER_CHANNEL_ID)
    counterMessage = await counterChannel.get_message(EGM_COUNTER_MESSAGE_ID)
    dayMessage = await counterChannel.get_message(EGM_DAYS_MESSAGE_ID)
    await counterMessage.edit(content = 0)
    await dayMessage.edit(content = datetime.date.today())

# Removed this feature as it spammed the committee
# If commitee member is @'d respond with @committee
mentionedCommitee = False
for x in message.mentions:
    for y in x.roles:
        if y.id == COMMITTEE_ROLE_ID:
            roles = client.get_guild(GAMESOC_GUILD_ID).roles
            for i in roles:
                if i.id == COMMITTEE_ROLE_ID:
                    if mentionedCommitee == False:
                        await message.channel.send(i.mention)
                        mentionedCommitee = True
