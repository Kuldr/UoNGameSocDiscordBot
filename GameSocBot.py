import discord
import asyncio
from login import TOKEN

#===============================CONSTANT-ISH====================================
# Misc
MESSAGE_TO_REACT_TO_ID = 490888395242078218
GAMESOC_GUILD_ID = 114348469241643011
ROLEALLOCATION_CHANNEL_ID = 490887919490433026
# Emoji IDs
LEAGUE_EMOJI_ID = 490883189896642560
DOTA_EMOJI_ID = 490883165884514334
OVERWATCH_EMOJI_ID = 490883226454327316
CSGO_EMOJI_ID = 612055189121138688
ROCKET_LEAGUE_EMOJI_ID = 490883269605195788
HEARTHSTONE_EMOJI_ID = 490883182397227009
RAINBOW_SIX_EMOJI_ID = 490883260193177640
PUBG_EMOJI_ID = 490883251142000640
FG_EMOJI_ID = 612061212812902453
WOW_EMOJI_ID = 613489408133562368
FORTNITE_EMOJI_ID = 490883173551570945
DESTINY_EMEOJI_ID = 612077075356057628
# Role IDs
LEAGUE_ROLE_ID = 613487966316134411
DOTA_ROLE_ID = 613488090933231655
OVERWATCH_ROLE_ID = 613488209057415198
CSGO_ROLE_ID = 613488370919800950
ROCKET_LEAGUE_ROLE_ID = 613488595054886951
HEARTHSTONE_ROLE_ID = 613488708490100757
RAINBOW_SIX_ROLE_ID = 613488853738717195
PUBG_ROLE_ID = 613488962576711691
FG_ROLE_ID = 613493086357815296
WOW_ROLE_ID = 613492918946103336
FORTNITE_ROLE_ID = 613489034261430376
DESTINY_ROLE_ID = 613489114851049491
# MISC
GAMESOCBOT_ROLE_ID = 490890046405345312

#==============================GLOBAL VARS======================================

client = discord.Client()

#===============================================================================

# Helper function that adds the specified role (w/ role_id) to the user
async def add_role_from_id(member, role_id):
    roles = client.get_guild(GAMESOC_GUILD_ID).roles
    for i in roles:
        if i.id == role_id:
            await member.add_roles(i)

# Helper function that removes the specified role (w/ role_id) to the user
async def remove_role_from_id(member, role_id):
    roles = client.get_guild(GAMESOC_GUILD_ID).roles
    for i in roles:
        if i.id == role_id:
            await member.remove_roles(i)

# When the client is set up and conneted it will print to the system running
#   the bot that it has connected
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# If a user reacts to the correct message, gives the user the relevant role
#   or removes the reaction
@client.event
async def on_raw_reaction_add(payload):
    # Need to make bot not react to its own reactions
    if client.user.id != payload.user_id:
        # Check that the reaction was added to the message that I want to checks
        if payload.message_id == MESSAGE_TO_REACT_TO_ID:
            reactionID = payload.emoji.id
            member = client.get_guild(payload.guild_id).get_member(payload.user_id)
            print("reacted to correct message")
            # Check to see which reaction was added
            # When a recognised reaction is added give the user the relevant role
            if reactionID == LEAGUE_EMOJI_ID:
                print("Reacted League")
                await add_role_from_id(member, LEAGUE_ROLE_ID)
            elif reactionID == DOTA_EMOJI_ID:
                print("Reacted DotA")
                await add_role_from_id(member, DOTA_ROLE_ID)
            elif reactionID == OVERWATCH_EMOJI_ID:
                print("Reacted OW")
                await add_role_from_id(member, OVERWATCH_ROLE_ID)
            elif reactionID == CSGO_EMOJI_ID:
                print("Reacted CSGO")
                await add_role_from_id(member, CSGO_ROLE_ID)
            elif reactionID == ROCKET_LEAGUE_EMOJI_ID:
                print("Reacted Rocket League")
                await add_role_from_id(member, ROCKET_LEAGUE_ROLE_ID)
            elif reactionID == HEARTHSTONE_EMOJI_ID:
                print("Reacted Hearthstone")
                await add_role_from_id(member, HEARTHSTONE_ROLE_ID)
            elif reactionID == RAINBOW_SIX_EMOJI_ID:
                print("Reacted Rainbow Six Siege")
                await add_role_from_id(member, RAINBOW_SIX_ROLE_ID)
            elif reactionID == PUBG_EMOJI_ID:
                print("Reacted PUBG")
                await add_role_from_id(member, PUBG_ROLE_ID)
            elif reactionID == FG_EMOJI_ID:
                print("Reacted Fighting Game")
                await add_role_from_id(member, FG_ROLE_ID)
            elif reactionID == WOW_EMOJI_ID:
                print("Reacted PUBG")
                await add_role_from_id(member, WOW_ROLE_ID)
            elif reactionID == FORTNITE_EMOJI_ID:
                print("Reacted Fortnite")
                await add_role_from_id(member, FORTNITE_ROLE_ID)
            elif reactionID == DESTINY_EMEOJI_ID:
                print("Reacted Destiny")
                await add_role_from_id(member, DESTINY_ROLE_ID)
            else:
                # Remove the reaction that is not relevant
                # channel = client.get_channel(payload.channel_id)
                message = await client.get_channel(ROLEALLOCATION_CHANNEL_ID).fetch_message(MESSAGE_TO_REACT_TO_ID)
                await message.remove_reaction(payload.emoji, member)
                print("Reaction not in list; Removing reaction")

# If a user removes react to the correct message, removes the role from the user
@client.event
async def on_raw_reaction_remove(payload):
        # Need to make bot not react to its own reactions
        if client.user.id != payload.user_id:
            # Check that the reaction was remove to the message that I want to checks
            if payload.message_id == MESSAGE_TO_REACT_TO_ID:
                reactionID = payload.emoji.id
                member = client.get_guild(payload.guild_id).get_member(payload.user_id)
                print("removed reacted to correct message")
                # Check to see which reaction was added
                # When a recognised reaction is added give the user the relevant role
                if reactionID == LEAGUE_EMOJI_ID:
                    print("Reacted League")
                    await remove_role_from_id(member, LEAGUE_ROLE_ID)
                elif reactionID == DOTA_EMOJI_ID:
                    print("Reacted DotA")
                    await remove_role_from_id(member, DOTA_ROLE_ID)
                elif reactionID == OVERWATCH_EMOJI_ID:
                    print("Reacted OW")
                    await remove_role_from_id(member, OVERWATCH_ROLE_ID)
                elif reactionID == CSGO_EMOJI_ID:
                    print("Reacted CSGO")
                    await remove_role_from_id(member, CSGO_ROLE_ID)
                elif reactionID == ROCKET_LEAGUE_EMOJI_ID:
                    print("Reacted Rocket League")
                    await remove_role_from_id(member, ROCKET_LEAGUE_ROLE_ID)
                elif reactionID == HEARTHSTONE_EMOJI_ID:
                    print("Reacted Hearthstone")
                    await remove_role_from_id(member, HEARTHSTONE_ROLE_ID)
                elif reactionID == RAINBOW_SIX_EMOJI_ID:
                    print("Reacted Rainbow Six Siege")
                    await remove_role_from_id(member, RAINBOW_SIX_ROLE_ID)
                elif reactionID == PUBG_EMOJI_ID:
                    print("Reacted PUBG")
                    await remove_role_from_id(member, PUBG_ROLE_ID)
                elif reactionID == FG_EMOJI_ID:
                    print("Reacted Fighting Game")
                    await remove_role_from_id(member, FG_ROLE_ID)
                elif reactionID == WOW_EMOJI_ID:
                    print("Reacted PUBG")
                    await remove_role_from_id(member, WOW_ROLE_ID)
                elif reactionID == FORTNITE_EMOJI_ID:
                    print("Reacted Fortnite")
                    await remove_role_from_id(member, FORTNITE_ROLE_ID)
                elif reactionID == DESTINY_EMEOJI_ID:
                    print("Reacted Destiny")
                    await remove_role_from_id(member, DESTINY_ROLE_ID)

#Simple command to check the server size
@client.event
async def on_message(message):
    # Makes sure the bot can't respond to itself
    if client.user.id != message.author.id:
        if message.content.upper() == "GSB?SERVERSIZE" or message.content.upper() == "GSB!SERVERSIZE":
            server = message.guild
            await message.channel.send(len(server.members))

# Run the bot with the token provided
client.run(TOKEN)
