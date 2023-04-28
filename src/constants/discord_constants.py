from src.constants.copypastas import NIGHTS_COPYPASTA, COACHELLA_COPYPASTA

SPAM_CHANNEL = 846304419335241759
JUST_CHATTING_CHANNEL = 488945733358321688
BOT_COMMANDS_CHANNEL = 751268873445048350
MUSIC_CHANNEL = 1058141992170823770
DEV_CHANNEL = 1062287061912129587

# Set of channels that bot can message in.
ALLOWED_CHANNELS = {
    SPAM_CHANNEL,
    BOT_COMMANDS_CHANNEL,
    MUSIC_CHANNEL,
    DEV_CHANNEL,
}

# If a message contains these trigger words, the bot will respond with a
# copypasta. The dictionary below maps trigger words to what copypasta
# the bot will respond with. The copypastas are located in the
# "copypasta.py" file within this directory.
BOT_TRIGGER_WORDS = {
    "frank": NIGHTS_COPYPASTA,
    "ocean": NIGHTS_COPYPASTA,
    "blonde": NIGHTS_COPYPASTA,
    "coachella": COACHELLA_COPYPASTA,
    "blink182": COACHELLA_COPYPASTA,
}
