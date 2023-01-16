import os
import random
import discord
import constants

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)


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
        and (any(word in message_content.split() for word in constants.BOT_TRIGGER_WORDS))


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

    # Allows bot to still react to commands even though we are overloading the on_message function.
    # See: https://stackoverflow.com/a/62380420
    await bot.process_commands(message)


@bot.command(name="trivia", aliases=["t"])
async def trivia(ctx: discord.ext.commands.context.Context) -> None:
    """
    When this command is triggered, it returns a trivia fact about Frank Ocean.

    :param ctx: Context object containing all relevant data about command being triggered.
    :return:    None.
    """
    if ctx.channel.id in constants.ALLOWED_CHANNELS:
        await ctx.send(random.choice(constants.TRIVIA))


@bot.command(name="song", aliases=["s"])
async def song(ctx) -> None:
    """
    When this command is triggered, it returns a random Frank Ocean song. The song is displayed in the format:
    "{song_title} from {album}: {link_to_song}" if the song is from an album or "{song_title} (Single): {link_to_song}"
    if the song is not from an album.

    :param ctx: Context object containing all relevant data about command being triggered.
    :return:    None.
    """
    if ctx.channel.id in constants.ALLOWED_CHANNELS:
        song = random.choice(constants.SONGS)
        # If the song is from an album we want to display "from {album_name}" after the song title, and if the
        # song is a single, we want to display "(Single)" after the song title.
        formatted_album = f"*({song.album})*" if song.album == "Single" else f"from *{song.album}*"
        await ctx.send(f"**{song.title}** {formatted_album}: {song.link}")


@bot.event
async def on_ready():
    print("Bot {0.user} is active".format(bot))


if __name__ == '__main__':
    bot.run(token)
