import datetime

import constants.coachella as coachella_date
import constants.discord_constants as discord_constants


def is_trigger_message(channel: int, message_content: str) -> bool:
    """
    Determines if a message sent by a user is a "trigger message". A message is a trigger message if the message
    contains any of the "trigger words" for the bot, which are defined in discord_constants.py and if the message is sent in
    one of the channels our bot is allowed to message in.

    :param channel:             The channel the message was sent in.
    :param message_content:     The content of the message
    :return:                    A boolean denoting if the message is a trigger message.
    """
    return (channel in discord_constants.ALLOWED_CHANNELS) \
        and (any(word in message_content.split() for word in discord_constants.BOT_TRIGGER_WORDS))


def get_days_until_coachella() -> int:
    """
    Returns the number of days until Frank Ocean performs at Coachella.

    :return:    An int representing the number of days until Frank Ocean performs at Coachella.
    """
    return (coachella_date.COACHELLA_FRANK_DATE - datetime.date.today()).days
