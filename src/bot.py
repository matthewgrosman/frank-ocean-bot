import os
import utils
import random
import discord

from dotenv import load_dotenv
from discord.ext import commands

import constants.songs as frank_songs
import constants.trivia as frank_trivia
import constants.lyrics as frank_lyrics
import constants.discord_constants as discord_constants

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, case_insensitive=True)


@bot.event
async def on_ready() -> None:
    """
    Prints a message to console when the bot connects to Discord.

    :return:    None.
    """
    print("Bot {0.user} is active.".format(bot))


@bot.event
async def on_message(message: discord.message.Message) -> None:
    """
    When a message is sent into a channel, this function will grab the message and determine if the bot
    should send a response. We send a response if the message contains any of the "trigger words" for the
    bot, which are defined in discord_constants.py and if the message is sent in one of the channels our bot is allowed
    to message in. If both of these conditions are met, the bot will respond with the Nights copypasta lol.

    :param message: A message sent in a Discord text channel.
    :return:        None.
    """
    # Ensure message is not from a bot
    if message.author == bot.user:
        return

    channel = message.channel.id
    user_message = str(message.content).lower()

    if utils.is_trigger_message(channel, user_message):
        await message.channel.send(frank_trivia.COACHELLA_COPYPASTA)

    # Allows bot to still react to commands even though we are overloading the on_message function.
    # See: https://stackoverflow.com/a/62380420
    await bot.process_commands(message)


@bot.command(name="trivia", aliases=["t"])
async def trivia(ctx: discord.ext.commands.context.Context) -> None:
    """
    Returns a fact about Frank Ocean.

    :param ctx: Context object containing all relevant data about command being triggered.
    :return:    None.
    """
    if ctx.channel.id in discord_constants.ALLOWED_CHANNELS:
        await ctx.send(random.choice(frank_trivia.TRIVIA))


@bot.command(name="song", aliases=["s"])
async def song(ctx: discord.ext.commands.context.Context) -> None:
    """
    Returns a Frank Ocean song or feature.

    The song is displayed in the format:
    "{song_title} from {album}: {link_to_song}" if the song is from an album or "{song_title} (Single): {link_to_song}"
    if the song is not from an album.

    :param ctx: Context object containing all relevant data about command being triggered.
    :return:    None.
    """
    if ctx.channel.id in discord_constants.ALLOWED_CHANNELS:
        song = random.choice(frank_songs.SONGS)
        # If the song is from an album we want to display "from {album_name}" after the song title, and if the
        # song is a single, we want to display "(Single)" after the song title.
        formatted_album = f"*({song.album})*" if song.album == "Single" else f"from *{song.album}*"
        await ctx.send(f"**{song.title}** {formatted_album}: {song.link}")


@bot.command(name="lyric", aliases=["l"])
async def trivia(ctx: discord.ext.commands.context.Context) -> None:
    """
    Returns a lyric from Frank Ocean.

    :param ctx: Context object containing all relevant data about command being triggered.
    :return:    None.
    """
    if ctx.channel.id in discord_constants.ALLOWED_CHANNELS:
        lyric = random.choice(frank_lyrics.LYRICS)
        await ctx.send(f"*{lyric.lyric}* (song: **{lyric.song}**)")


@bot.command(name="coachella", aliases=["c"])
async def coachella(ctx: discord.ext.commands.context.Context) -> None:
    """
    Returns days until Frank Ocean performs at Coachella.

    :param ctx: Context object containing all relevant data about command being triggered.
    :return:    None.
    """
    if ctx.channel.id in discord_constants.ALLOWED_CHANNELS:
        await ctx.send(f"**{utils.get_days_until_coachella()} days left until Frank Ocean performs at Coachella!!!!**")


@bot.command(name="picture", aliases=["p"])
async def picture(ctx: discord.ext.commands.context.Context) -> None:
    """
    Returns a picture of Frank Ocean.

    :param ctx: Context object containing all relevant data about command being triggered.
    :return:    None.
    """
    if ctx.channel.id in discord_constants.ALLOWED_CHANNELS:
        picture_directory = "images/"
        picture_file = random.choice(os.listdir(picture_directory))
        await ctx.send(file=discord.File(picture_directory + picture_file))


@bot.command(name="gif", aliases=["g"])
async def gif(ctx: discord.ext.commands.context.Context) -> None:
    """
    Returns a gif of Frank Ocean.

    :param ctx: Context object containing all relevant data about command being triggered.
    :return:    None.
    """
    if ctx.channel.id in discord_constants.ALLOWED_CHANNELS:
        gif_directory = "gifs/"
        gif_file = random.choice(os.listdir(gif_directory))
        await ctx.send(file=discord.File(gif_directory + gif_file))


if __name__ == '__main__':
    bot.run(token)
