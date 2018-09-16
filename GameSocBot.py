import discord
import asyncio
from login import TOKEN
import datetime

#===============================CONSTANT-ISH====================================
# Misc
MESSAGE_TO_REACT_TO_ID = 1
GAMESOC_GUILD_ID = 114348469241643011
EGM_COUNTER_CHANNEL_ID = 490853584347594764
EGM_COUNTER_MESSAGE_ID = 490854630927106049
EGM_DAYS_MESSAGE_ID = 490860539950530570
# Emoji IDs
OVERWATCH_EMOJI_ID = 490883226454327316
LEAGUE_EMOJI_ID = 490883189896642560
FORTNITE_EMOJI_ID = 490883173551570945
DOTA_EMOJI_ID = 490883165884514334
CSGO_EMOJI_ID = 490883131939749918
WOW_EMOJI_ID = 490883328959053824
ROCKET_LEAGUE_EMOJI_ID = 490883269605195788
HEARTHSTONE_EMOJI_ID = 490883182397227009
DESTINY_EMEOJI_ID = 490883146540253194
RAINBOW_SIX_EMOJI_ID = 490883260193177640
PUBG_EMOJI_ID = 490883251142000640
MTG_EMOJI_ID = 490883199044681742
WARFRAME_EMOJI_ID = 490883287556816896
# Role IDs
OVERWATCH_ROLE_ID = 360239768317067264
LEAGUE_ROLE_ID = 360239401839624214
FORTNITE_ROLE_ID = 420236263233159169
DOTA_ROLE_ID = 360464804865114115
CSGO_ROLE_ID = 360239648162709505
WOW_ROLE_ID = 370643554655141888
ROCKET_LEAGUE_ROLE_ID = 360465836852641792
HEARTHSTONE_ROLE_ID = 360467250634817536
DESTINY_ROLE_ID = 372823107905257492
RAINBOW_SIX_ROLE_ID = 420351992133582861
PUBG_ROLE_ID = 360238836623605760
MTG_ROLE_ID = 474253927278182410
WARFRAME_ROLE_ID = 488835550258659348
COMMITTEE_ROLE_ID = 471020920753094656

client = discord.Client()

#===============================================================================
# IDEAS
# Standard help command - pm help command
# Bot overview channel
# Playing bot!help for help
# GET ROLES VIA REACTIONS
# WEDNESDAY NIGHT PC GAMING RANDOMISE PLAYERS
# Shrek Super Slam
# Can I make it so that whenever I type in the terminal it will talk as the bot
#   Or maybe allow my bots to be controlled from a master server ???
# MAKE IT SO THAT IT WILL TALK TO PEOPLE
#===============================================================================

async def add_role_from_id(member, role_id):
    roles = client.get_guild(GAMESOC_GUILD_ID).roles
    for i in roles:
        if i.id == role_id:
            await member.add_roles(i)

# When the client is set up and conneted it will print to the system running
#   the bot that it has connected
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_raw_reaction_add(payload):
    # Check that the reaction was added to the message that I want to checks
    if payload.message_id == MESSAGE_TO_REACT_TO_ID:
        reactionID = payload.emoji.id
        member = client.get_guild(payload.guild_id).get_member(payload.user_id)
        print("reacted to correct message")
        # Check to see which reaction was added
        # When a recognised reaction is added give the user the relevant role
        if reactionID == OVERWATCH_EMOJI_ID:
            print("Reacted OW")
            await add_role_from_id(member, OVERWATCH_ROLE_ID)
        elif reactionID == LEAGUE_EMOJI_ID:
            print("Reacted League")
            await add_role_from_id(member, LEAGUE_ROLE_ID)
        elif reactionID == FORTNITE_EMOJI_ID:
            print("Reacted Fortnite")
            await add_role_from_id(member, FORTNITE_ROLE_ID)
        elif reactionID == DOTA_EMOJI_ID:
            print("Reacted DotA")
            await add_role_from_id(member, DOTA_ROLE_ID)
        elif reactionID == CSGO_EMOJI_ID:
            print("Reacted CSGO")
            await add_role_from_id(member, CSGO_ROLE_ID)
        elif reactionID == WOW_EMOJI_ID:
            print("Reacted WoW")
            await add_role_from_id(member, WOW_ROLE_ID)
        elif reactionID == ROCKET_LEAGUE_EMOJI_ID:
            print("Reacted Rocket League")
            await add_role_from_id(member, ROCKET_LEAGUE_ROLE_ID)
        elif reactionID == HEARTHSTONE_EMOJI_ID:
            print("Reacted Hearthstone")
            await add_role_from_id(member, HEARTHSTONE_ROLE_ID)
        elif reactionID == DESTINY_EMEOJI_ID:
            print("Reacted Destiny")
            await add_role_from_id(member, DESTINY_ROLE_ID)
        elif reactionID == RAINBOW_SIX_EMOJI_ID:
            print("Reacted Rainbow Six Siege")
            await add_role_from_id(member, RAINBOW_SIX_ROLE_ID)
        elif reactionID == PUBG_EMOJI_ID:
            print("Reacted PUBG")
            await add_role_from_id(member, PUBG_ROLE_ID)
        elif reactionID == MTG_EMOJI_ID:
            print("Reacted MTG")
            await add_role_from_id(member, MTG_ROLE_ID)
        elif reactionID == WARFRAME_EMOJI_ID:
            print("Reacted Warframe")
            await add_role_from_id(member, WARFRAME_ROLE_ID)
        else:
            # Remove the reaction that is not relevant
            channel = client.get_channel(payload.channel_id)
            message = await channel.get_message(490842813517529109)
            await message.remove_reaction(payload.emoji, member)
            print("Reaction not in list; Removing reaction")

#This is where all the on message events happen
@client.event
async def on_message(message):
    # Makes sure the bot can't respond to itself
    if client.user.id != message.author.id:
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

        # Reset counter command for EGM
        if message.content.upper() == "EGM?RESET" and message.channel.id == EGM_COUNTER_CHANNEL_ID:
            counterChannel = client.get_channel(EGM_COUNTER_CHANNEL_ID)
            counterMessage = await counterChannel.get_message(EGM_COUNTER_MESSAGE_ID)
            dayMessage = await counterChannel.get_message(EGM_DAYS_MESSAGE_ID)
            await counterMessage.edit(content = 0)
            await dayMessage.edit(content = datetime.date.today())

        # If an egm is mentioned increment counter and then respond to the message
        # This isn't perfect as there are some words that contain egm but so be it does it matter
        # Here is the list: https://www.wordfind.com/contains/Egm/
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


# Run the bot with the token provided
client.run(TOKEN)
