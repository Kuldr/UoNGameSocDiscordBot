import discord
import asyncio
from login import TOKEN
import datetime
import random

#===============================CONSTANT-ISH====================================
# Misc
MESSAGE_TO_REACT_TO_ID = 490888395242078218
GAMESOC_GUILD_ID = 114348469241643011
GAMESOC_GENERAL_CHANNEL_ID = 360502416631922690
KTR_GUILD_ID = 481147770254786561
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
GAMESOCBOT_ROLE_ID = 490890046405345312
GSBCOLOUR_ROLE_ID = 511575845165596696
# User IDs
ROMPAFROLIC_USER_ID = 140625437498802176
# Casino Stuff
BETTING_CHANNEL_ID = 0
SCORE_CHANNEL_ID = 0
startCasinoString = ("Howdy everyone, welcome to the betting ring!\n"
                     "For each fight there will be a new bet\n"
                     "If you wanna place a bet on either side react with ⬅️ or ➡️ accordingly\n"
                     "Every one starts with ₲1000 (G-bucks) and each bet costs ₲100\n"
                     "You will win a percentage of the prize pool based on the number of bets placed!\n"
                     "GL HF")
BETTING_MESSAGE_ID = 0
BETTING_RESPONCE_MESSAGE_ID = 0 # MAYBE IMPLEMENT THIS
SCORE_MESSAGE_ID = 0
SCORES = {140625437498802176: 2000, 482545753970049034: 1000, 212960804792827904: 3000} #Form {ID : SCORE}
BETS = {} #Form {ID : SIDE} SIDE is either "L" or "R"
BETTING_OPEN = False

#==============================GLOBAL VARS======================================

client = discord.Client()

#===============================================================================
# IDEAS
# Standard help command - pm help command
# Bot overview channel
# Playing bot!help for help
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

async def addBet(userID, bet):
    if BETTING_OPEN:
        if userID not in BETS: # Check they haven't already made a bet
            SCORES[userID] -= 100
            BETS[userID] = bet
            await updateScores()

async def updateScores():
    scoreChannel = client.get_channel(SCORE_CHANNEL_ID)
    scoreMessage = await scoreChannel.get_message(SCORE_MESSAGE_ID)

    sortedScores = [(k, SCORES[k]) for k in sorted(SCORES, key=SCORES.get, reverse=True)]
    s = "```₲12345 | Username\n-----------------\n"
    for key, value in sortedScores:
        usernick = client.get_user(key).display_name
        s = s + "₲" + str(value) + " "*(5-len(str(value))) + " | " + usernick + "\n" #key needs to be made into something usable
    s = s + "```"


    # Build up the string to send in the message
    # ₲12345 | Username
    # s = "```₲12345 | Username\n-----------------\n"
    # for key, value in SCORES.items():
    #     usernick = client.get_user(key).display_name
    #     s = s + "₲" + str(value) + " "*(5-len(str(value))) + " | " + usernick + "\n" #key needs to be made into something usable
    # s = s + "```"
    # Edit the message with the new message
    await scoreMessage.edit(content = s)

# async def colourChanger():
#     await client.wait_until_ready()
#     role = client.get_guild(GAMESOC_GUILD_ID).get_role(GSBCOLOUR_ROLE_ID)
#     while not client.is_closed():
#         r = random.randint(0, 0xFFFFFF)
#         await role.edit(colour = discord.Colour(r))
#         # await asyncio.sleep(1)
#         # Currently doesn't limit the time between role colour updates

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
    # Need to make bot not react to its own reactions
    if client.user.id != payload.user_id:
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
                message = await channel.get_message(MESSAGE_TO_REACT_TO_ID)
                await message.remove_reaction(payload.emoji, member)
                print("Reaction not in list; Removing reaction")
        elif payload.message_id == BETTING_MESSAGE_ID:
            global SCORES
            global BETS
            reactionName = payload.emoji.name
            # Check to see which reaction was added
            # When a recognised reaction is added respond to it
            if reactionName == "\U000027A1":
                userID = payload.user_id
                if userID in SCORES: # Check if the user has a score
                    await addBet(userID, "R")
                else:
                    SCORES[userID] = 1000
                    await addBet(userID, "R")
            elif reactionName == "\U00002B05":
                userID = payload.user_id
                if userID in SCORES: # Check if the user has a score
                    await addBet(userID, "L")
                else:
                    SCORES[userID] = 1000
                    await addBet(userID, "L")
            else:
                # Remove the reaction that is not relevant
                channel = client.get_channel(payload.channel_id)
                message = await channel.get_message(BETTING_MESSAGE_ID)
                await message.remove_reaction(payload.emoji, client.get_guild(payload.guild_id).get_member(payload.user_id))
                print("Reaction not in list; Removing reaction")


#This is where all the on message events happen
@client.event
async def on_message(message):
    # Makes sure the bot can't respond to itself
    if client.user.id != message.author.id:
        if message.content.upper() == "GSB?SERVERSIZE" or message.content.upper() == "GSB!SERVERSIZE":
            server = message.guild
            await message.channel.send(len(server.members))
        # 1% chance of responding to a message from rupert with /s
        elif message.author.id == ROMPAFROLIC_USER_ID:
            if random.random() < 0.05:
                await message.channel.send("/s")

        # Casino stuff
        elif message.content.upper() == "GSB?STARTCASINO" or message.content.upper() == "GSB!STARTCASINO":
            global BETTING_CHANNEL_ID
            global SCORE_CHANNEL_ID
            global SCORE_MESSAGE_ID
            if BETTING_CHANNEL_ID == 0:
                gameSocServer = client.get_guild(KTR_GUILD_ID)
                casinoCategory = await gameSocServer.create_category("GameSoc Casino")
                bettingChannel = await gameSocServer.create_text_channel('Casino Floor', category = casinoCategory)
                scoreChannel = await gameSocServer.create_text_channel('High Rollers', category = casinoCategory)
                await gameSocServer.create_text_channel('Casino Lounge', category = casinoCategory)
                BETTING_CHANNEL_ID = bettingChannel.id
                SCORE_CHANNEL_ID = scoreChannel.id
                everyone = client.get_guild(KTR_GUILD_ID).default_role
                await bettingChannel.set_permissions(everyone, read_messages=True, send_messages=False)
                await scoreChannel.set_permissions(everyone, read_messages=True, send_messages=False, add_reactions=False) #SET TO NO REACTIONS
                await bettingChannel.send(startCasinoString)
                scoreMessage = await scoreChannel.send("```₲12345 | Username\n-----------------\n```")
                SCORE_MESSAGE_ID = scoreMessage.id
            else:
                print("Casino is already open")
        elif message.content.upper().startswith("GSB?STARTNEWFIGHT") or message.content.upper().startswith("GSB!STARTNEWFIGHT"):
            if BETTING_CHANNEL_ID == 0:
                print("Start the casino")
            else:
                global BETTING_MESSAGE_ID
                global BETS
                global BETTING_OPEN
                BETS = {}
                BETTING_OPEN = True
                bettingChannel = client.get_channel(BETTING_CHANNEL_ID)
                betMessage = await bettingChannel.send("React ⬅️ or ➡️ to place your bet")
                BETTING_MESSAGE_ID = betMessage.id
                await betMessage.add_reaction("\U00002B05")
                await betMessage.add_reaction("\U000027A1")
        elif message.content.upper().startswith("GSB?ENDFIGHT") or message.content.upper().startswith("GSB!ENDFIGHT"):
            global SCORES
            if message.content.upper() == "GSB?ENDFIGHT L" or message.content.upper() == "GSB!ENDFIGHT L":
                prizePool = (len(BETS)+1)*100
                # Find number of the winners
                winners = 0
                for key, value in BETS.items():
                    if value == "L":
                        winners += 1
                for key, value in BETS.items():
                    if value == "L":
                        SCORES[key] += prizePool/winners
            elif message.content.upper() == "GSB?ENDFIGHT R" or message.content.upper() == "GSB!ENDFIGHT R":
                prizePool = (len(BETS)+1)*100
                # Find number of the winners
                winners = 0
                for key, value in BETS.items():
                    if value == "R":
                        winners += 1
                for key, value in BETS.items():
                    if value == "R":
                        SCORES[key] += prizePool/winners
            else:
                print("YOU DIDN'T SAY WHO WON")
            await updateScores()
        elif message.content.upper() == "GSB?CLOSEBETTING" or message.content.upper() == "GSB!CLOSEBETTING":
            BETTING_OPEN = False
            bettingChannel = client.get_channel(BETTING_CHANNEL_ID)
            bettingMessage = await bettingChannel.get_message(BETTING_MESSAGE_ID)
            await bettingMessage.edit(content = "Betting for this fight is now closed! Enjoy the fight")
        elif message.content.upper() == "GSB?UPDATESCORES" or message.content.upper() == "GSB!UPDATESCORES":
            if SCORE_CHANNEL_ID == 0:
                print("Start the casino")
            else:
                await updateScores()

#Start the background task looking for a new spheal
# client.loop.create_task(colourChanger())

# Run the bot with the token provided
client.run(TOKEN)
