import random
import datetime

from .trivia import TRIVIA
from .coachella import COACHELLA_FRANK_DATE


def get_weekly_update_message() -> str:
    """
    This is being made into a function rather than a simple string because we need to
    use the datetime.date.today() function call.

    If we simply left this as a string, the value of datetime.date.today() would be
    cached after the first instance of the string being used. This is an issue as we
    want datetime.date.today() to be called each time we want the string, not to be
    pulling from a cache of an out of date timestamp.

    The solution here is to create a function that returns the string. The function
    scope will be ran each time the function is called, we can generate a fresh
    datetime.date.today() result each time.
    :return:
    """
    today = datetime.date.today()
    trivia = random.choice(TRIVIA)
    return "**HELLO FELLOW FRANK OCEAN FANS!!!!** It is time for another weekly Frank Ocean fun " \
           f"fact!\n\n*Frank Ocean fun fact of the day*: {trivia} \n\nWow, what an " \
           f"incredible fact. And now it's time for the **WEEKLY COACHELLA COUNTDOWN**: There are " \
           f"only **{(COACHELLA_FRANK_DATE - today).days} days left** until Frank Ocean performs " \
           f"at Coachella!!! FRANKCHELLA APPROACHES SOON.\n\nHave a fantastic day everyone :)"
