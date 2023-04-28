import constants.discord_constants as discord_constants


def is_message_from_allowed_channel(channel: int) -> bool:
    """
    Checks if the channel a message was sent from is an allowed channel. An
    allowed channel means the bot is allowed to send messages into the channel.
    We use this function to help determine if the bot can send a message.

    :param channel: An int denoting the channel ID that a message was sent in.
    :return:        A boolean denoting if the channel ID param is in the allowed
                    channel list.
    """
    return channel in discord_constants.ALLOWED_CHANNELS


def get_trigger_words_from_message(message_content: str) -> set:
    """
    Parses a user message and keeps track of any trigger words that were said.
    Returns a set containing all the trigger words found in the message.

    :param message_content: A string denoting the content of the message.
    :return:                A set containing all the trigger words found in
                            the message.
    """
    trigger_words = set()

    for word in message_content.split():
        if word in discord_constants.BOT_TRIGGER_WORDS:
            trigger_words.add(word)

    return trigger_words
