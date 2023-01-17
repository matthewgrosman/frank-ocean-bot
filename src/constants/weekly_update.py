import random

from .trivia import TRIVIA
from src import utils


WEEKLY_UPDATE_MESSAGE = "**HELLO FELLOW FRANK OCEAN FANS!!!!** It is time for another weekly Frank Ocean fun " \
                f"fact!\n\n*Frank Ocean fun fact of the day*: {random.choice(TRIVIA)} \n\nWow, what an " \
                f"incredible fact. And now it's time for the **WEEKLY COACHELLA COUNTDOWN**: There are " \
                f"only **{utils.get_days_until_coachella()} days left** until Frank Ocean performs at Coachella!!! " \
                f"FRANKCHELLA APPROACHES SOON.\n\nHave a fantastic day everyone :)"
