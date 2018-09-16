import discord
import asyncio
from login import TOKEN

# Constant-ish :P
MESSAGE_TO_REACT_TO_ID = 490627055004942337
GUILD_ID = 481147770254786561
OVERWATCH_EMOJI_ID = 490191693111492628
LEAGUE_EMOJI_ID = 1
FORTNITE_EMOJI_ID = 1
DOTA_EMOJI_ID = 1
CSGO_EMOJI_ID = 490191622936461332
WOW_EMOJI_ID = 1
ROCKET_LEAGUE_EMOJI_ID = 1
HEARTHSTONE_EMOJI_ID = 1
DESTINY_EMEOJI_ID = 1
RAINBOW_SIX_EMOJI_ID = 1
PUBG_EMOJI_ID = 1
MTG_EMOJI_ID = 1
WARFRAME_EMOJI_ID = 1
OVERWATCH_ROLE_ID = 490191693111492628
LEAGUE_ROLE_ID = 1
FORTNITE_ROLE_ID = 1
DOTA_ROLE_ID = 1
CSGO_ROLE_ID = 490191622936461332
WOW_ROLE_ID = 1
ROCKET_LEAGUE_ROLE_ID = 1
HEARTHSTONE_ROLE_ID = 1
DESTINY_ROLE_ID = 1
RAINBOW_SIX_ROLE_ID = 1
PUBG_ROLE_ID = 1
MTG_ROLE_ID = 1
WARFRAME_ROLE_ID = 1
COMMITTEE_ROLE_ID = 482211682865774592

#TODO CHECK WHICH ROLES ALREADY HAVE AN ICON
#TODO WORK OUT WHAT VALUES I NEED TO GRAB AND HOW
#TODO CLEAR REACTIONS IF TOO MANY; WHAT IS TOO MANY

client = discord.Client()

#===============================================================================
# IDEAS
# Standard help command - pm help command
# Bot overview channel
# Playing bot!help for help
# GET ROLES VIA REACTIONS
# WEDNESDAY NIGHT PC GAMING RANDOMISE PLAYERS
# EGM Counter
# Shrek Super Slam
# YOU NEVER SEE IT COMING - MAYBE MAKE THIS AS A SEPERATE VOICE BOT
# Can I make it so that whenever I type in the terminal it will talk as the bot
#   Or maybe allow my bots to be controlled from a master server ???
# MAKE IT SO THAT IT WILL TALK TO PEOPLE
# MULTICOLOUR NAME :P
#===============================================================================

async def add_role_from_id(member, role_id):
    roles = client.get_guild(GUILD_ID).roles
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
            print("Reaction not in list")
            print(reactionID)

# Do users need some verification ?? probs not
# Warn people that if they had old roles then unreacting won't work? Commitee is fail safe, could react un react work

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
                    roles = client.get_guild(GUILD_ID).roles
                    for i in roles:
                        if i.id == COMMITTEE_ROLE_ID:
                            if mentionedCommitee == False:
                                await message.channel.send(i.mention)
                                mentionedCommitee = True


# Run the bot with the token provided
client.run(TOKEN)
