import os
import discord
import constants

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents, case_insensitive=True)


def is_trigger_message(channel: int, message_content: str) -> bool:
    """
    Determines if a message sent by a user is a "trigger message". A message is a trigger message if the message
    contains any of the "trigger words" for the bot, which are defined in constants.py and if the message is sent in
    one of the channels our bot is allowed to message in.

    :param channel:             The channel the message was sent in.
    :param message_content:     The content of the message
    :return:                    A boolean denoting if the message is a trigger message.
    """
    return (channel in constants.ALLOWED_CHANNELS) \
        and (any(word in message_content for word in constants.BOT_TRIGGER_WORDS))


@bot.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(bot))


@bot.event
async def on_message(message: discord.message.Message) -> None:
    """
    When a message is sent into a channel, this function will grab the message and determine if the bot
    should send a response. We send a response if the message contains any of the "trigger words" for the
    bot, which are defined in constants.py and if the message is sent in one of the channels our bot is allowed
    to message in. If both of these conditions are met, the bot will respond with the Nights copypasta lol.

    :param message: A message sent in a Discord text channel.
    :return:        None.
    """
    # Ensure message is not from a bot
    if message.author == bot.user:
        return

    channel = message.channel.id
    user_message = str(message.content).lower()

    if is_trigger_message(channel, user_message):
        await message.channel.send(constants.NIGHTS_COPYPASTA)


if __name__ == '__main__':
    bot.run(token)
