import discord
import asyncio
from login import TOKEN

# Constants-ish
BOT_CHANNEL_NAME = "talk-to-bot"

client = discord.Client()

#===============================================================================
# IDEAS
# WEDNESDAY NIGHT PC GAMING RANDOMISE PLAYERS
# EGM Counter
# Shrek Super Slam
#===============================================================================


# When the client is set up and conneted it will print to the system running
#   the bot that it has connected
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#This is where all the on message events happen
@client.event
async def on_message(message):
    # Makes sure the bot can't respond to itself
    if client.user.id != message.author.id:
        print(message.content)

        # If the bot is being issued a command checks to see if its in the correct channel
        #   This will hopefully avoid spam
        if message.content.startswith('!') or message.content.startswith('?'):
            if message.channel.name != BOT_CHANNEL_NAME:
                botChannel = discord.utils.get(client.get_all_channels(), name=BOT_CHANNEL_NAME)
                await client.send_message(botChannel, "pssst <@%s> talk to me over here" % (message.author.id))

            elif message.content.upper().startswith('!ADDROLE') or message.content.upper().startswith('?ADDROLE'):
                tmp = await client.send_message(message.channel, 'Adding Role...')
                member = message.author

                args = message.content.split(" ")

                for roleArg in args[1:]:
                    role = discord.utils.get(member.server.roles, name = roleArg)
                    if role == None:
                        await client.send_message(message.channel, "<@%s> We do not have role %s" % ((member.id), roleArg))
                    elif role.name == "committee":
                        await client.send_message(message.channel, "<@%s> I cannot give you the role %s" % ((member.id), roleArg))
                    else:
                        await client.add_roles(member, role)
                await client.edit_message(tmp, "<@%s> I have added the requested roles for you!" % (member.id))

            else:
                await client.send_message(message.channel, 'Command not recognised')

# Run the bot with the token provided
client.run(TOKEN)
