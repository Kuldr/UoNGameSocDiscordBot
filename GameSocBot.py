import discord
import asyncio
from login import TOKEN

#===============================CONSTANT-ISH====================================
# Misc
MESSAGE_TO_REACT_TO_ID = 490888395242078218
GAMESOC_GUILD_ID = 114348469241643011
# Emoji IDs
LEAGUE_EMOJI_ID = 490883189896642560
DOTA_EMOJI_ID = 490883165884514334
OVERWATCH_EMOJI_ID = 490883226454327316
CSGO_EMOJI_ID = 612055189121138688
ROCKET_LEAGUE_EMOJI_ID = 490883269605195788
HEARTHSTONE_EMOJI_ID = 490883182397227009
RAINBOW_SIX_EMOJI_ID = 490883260193177640
PUBG_EMOJI_ID = 490883251142000640
FORTNITE_EMOJI_ID = 490883173551570945
DESTINY_EMEOJI_ID = 612077075356057628
# Role IDs
LEAGUE_ROLE_ID = 360239401839624214
DOTA_ROLE_ID = 360464804865114115
OVERWATCH_ROLE_ID = 360239768317067264
CSGO_ROLE_ID = 360239648162709505
ROCKET_LEAGUE_ROLE_ID = 360465836852641792
HEARTHSTONE_ROLE_ID = 360467250634817536
RAINBOW_SIX_ROLE_ID = 420351992133582861
PUBG_ROLE_ID = 360238836623605760
FORTNITE_ROLE_ID = 420236263233159169
DESTINY_ROLE_ID = 372823107905257492
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
            elif reactionID == FORTNITE_EMOJI_ID:
                print("Reacted Fortnite")
                await add_role_from_id(member, FORTNITE_ROLE_ID)
            elif reactionID == DESTINY_EMEOJI_ID:
                print("Reacted Destiny")
                await add_role_from_id(member, DESTINY_ROLE_ID)
            else:
                # Remove the reaction that is not relevant
                channel = client.get_channel(payload.channel_id)
                message = await channel.get_message(MESSAGE_TO_REACT_TO_ID)
                await message.remove_reaction(payload.emoji, member)
                print("Reaction not in list; Removing reaction")

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
