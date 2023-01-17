import random
import datetime

from .trivia import TRIVIA
from .coachella import COACHELLA_FRANK_DATE


WEEKLY_UPDATE_MESSAGE = "**HELLO FELLOW FRANK OCEAN FANS!!!!** It is time for another weekly Frank Ocean fun " \
                f"fact!\n\n*Frank Ocean fun fact of the day*: {random.choice(TRIVIA)} \n\nWow, what an " \
                f"incredible fact. And now it's time for the **WEEKLY COACHELLA COUNTDOWN**: There are " \
                f"only **{(COACHELLA_FRANK_DATE - datetime.date.today()).days} days left** until Frank Ocean performs " \
                f"at Coachella!!! FRANKCHELLA APPROACHES SOON.\n\nHave a fantastic day everyone :)"
