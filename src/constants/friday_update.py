import random
import src.constants.trivia as frank_trivia

from src import utils


FRIDAY_UPDATE = "**HAPPY FRIDAY** FELLOW FRANK OCEAN FANS!!!! It is time for another Frank Ocean Friday fun " \
                f"fact.\nFrank fun fact of the day: {random.choice(frank_trivia.TRIVIA)} Wow, what an " \
                f"incredible fact. And now it's time for the **WEEKLY COACHELLA COUNTDOWN!!!!!!**.\nThere are " \
                f" only {utils.get_days_until_coachella()} days left until Frank Ocean performs at Coachella!!!"
