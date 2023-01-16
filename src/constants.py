from collections import namedtuple

# Set of channels that bot can message in.
ALLOWED_CHANNELS = {
    846304419335241759,     # spam
    488945733358321688,     # just-chatting
    751268873445048350,     # bot-commands
    1058141992170823770,    # music
    1062287061912129587,    # random (DEV ACCOUNT, REMOVE THIS LATER)
}

# If a message contains these words, the bot will respond with the Nights copypasta.
BOT_TRIGGER_WORDS = {"frank", "ocean", "blonde"}

# A copypasta talking about how Nights contains a beat switch halfway through the album Blonde.
NIGHTS_COPYPASTA = "Did you know that on the album Blonde (2016) by artist Frank Ocean, at *exactly* halfway through " \
                    "the album’s one hour runtime a beat switch occurs on the track Nights? There are many different " \
                    "interpretations on the meaning behind this. Some theories link it back to the album’s " \
                    "exploration of the duality in our lives: youthfulness vs. aging, reality vs. how we remember " \
                    "the past- even the spelling of the album’s title (Blonde vs Blond) varies across streaming " \
                    "platforms and physical vinyl releases. "

# This list contains trivia about Frank Ocean. This is where the "!trivia" command pulls trivia from.
TRIVIA = [
    "Frank Ocean wrote *Channel Orange* in just **2 weeks**!",
    "Frank Ocean eats his Pop-Tarts without frosting.",
    "One day before releasing *Blonde*, Frank Ocean released a visual album titled *ENDLESS*. Releasing *ENDLESS* "
    "allowed Frank to fulfill his contract with DefJam requiring one more album, which meant he could release Blonde "
    "under his independent record label *Boys Don't Cry*. It is estimated that Frank netted $20 million off of Blonde "
    "by cutting DefJam out.",
    "Frank recorded **50 versions** of the song *White Ferrari*.",
    "In 2014, Frank backed out of an agreement with Chipotle to cover a song for an advertisement. Chipotle sued "
    "Frank for $212,500 (the amount of his advance). Frank sent a check to Chipotle for the exact amount, with the "
    "memo reading 'FUCK OFF'.",
    "'Frank Ocean' was originally just a stage name! Frank Ocean's birth name is Christopher Breaux. He legally changed"
    " his name to Frank Ocean in 2015.",
    "Frank listed his dog Everest as an executive producer on *Channel Orange*.",
    "Frank was born in Long Beach, California.",
    "Frank dropped out of college after his freshman year to focus on making music.",
    "Chris Brown and friends jumped Frank Ocean over a parking spot.",
    "Frank Ocean is, in fact, not an ocean.",
    "There is a version of *Nights* that features Kendrick Lamar: https://www.youtube.com/watch?v=RQen_iqPIEM",
    "When Blonde released, Frank set up a couple pop-up shops around the world that handed out magazines titled "
    "'Boys Don't Cry'. These magazines contain tons of cool visuals and writings, in addition to a special CD version "
    "of Blonde. This CD version contained some differences on a couple of tracks",
    "Frank is reportedly working on a movie or some visual project with studio A24.",
    "Frank Ocean was born on October 28, 1987.",
    "Frank Ocean was a part of rap group ODD FUTURE",
    "Frank Ocean's record label is called 'Boys Don't Cry', which was the original name for *Blonde*",
    "Frank Ocean released a song titled *Memrise* on Tumblr. This song was originally intended to be used in the movie "
    "*Django Unchained*. Quintin Tarantino described the song as 'truly lovely and poetic in every way', but was unable"
    " to find a scene where the song fit correctly.",
    "Frank credits *The Beatles* on song White Ferrari for referencing a melody from one of their songs.",
    "There is a version of *Chanel* featuring A$AP Rocky: https://www.youtube.com/watch?v=MRyNOYrt6Wc",
    "There is a version of *Lens* featuring Travis Scott: https://www.youtube.com/watch?v=HE6hpNS2i6Y",
    "Frank Ocean's merch team accidentally shipped out a vinyl for an unreleased song titled *These Days* to a handful "
    "of customers who ordered merch from Frank's site. When discovered, the merch team immediately contacted those with"
    " the unreleased vinyl and offered them an *ENDLESS* vinyl in exchange for retuning the unreleased song. To this "
    "day, nobody leaked the track from the vinyl and it's contents are unknown...:  "
    "https://www.reddit.com/r/FrankOcean/comments/qpywb2/yall_remember_these_days/",
    "Frank Ocean's Reddit account was u/granddaddywasaplayer. Frank recently deleted the entire account.",
    "Frank recorded a song with artist Skepta titled *Little Demon*. This was originally planned for a vinyl release "
    "but was scrapped at the last minute. There is still no high quality version of *Little Demon* on the internet.",
    "Frank Ocean's first performance was at Coachella in 2011 where he performed with ODD FUTURE.",
    "In 2013, Frank performed a concert in Germany, where he sang a few early versions of songs that would later be "
    "on Blonde 3 years later! Here is a video of an early version of *Ivy*: https://www.youtube.com/watch?v=X-q_e2HqSiI",
    "Frank Ocean lives in New York City.",
    "Before recording his own music, Frank Ocean was originally a songwriter. He has written songs for artists such as "
    "Justin Bieber and Beyonce.",
    NIGHTS_COPYPASTA
]


# This list contains Frank Ocean songs or features. Each of these contains the track name, album and link to the song.
# This is where the "!song" command pulls from.
Song = namedtuple("Song", ["title", "album", "link"])
SONGS = [
    # Nostalgia Ultra
    Song("Strawberry Swing", "nostalgia, ULTRA", "https://www.youtube.com/watch?v=G7wcRZWRDdw"),
    Song("Novacane", "nostalgia, ULTRA", "https://open.spotify.com/track/4osgfFTICMkcGbbigdsa53?si=718e622f6a32475d"),
    Song("We All Try", "nostalgia, ULTRA", "https://shorturl.at/ceGRX"),
    Song("Songs for Women", "nostalgia, ULTRA", "https://shorturl.at/alrC0"),
    Song("Lovecrimes", "nostalgia, ULTRA", "https://shorturl.at/tAFQU"),
    Song("There Will Be Tears", "nostalgia, ULTRA", "https://shorturl.at/ipVX4"),
    Song("Dust", "nostalgia, ULTRA", "https://shorturl.at/dTZ01"),
    Song("Nature Feels", "nostalgia, ULTRA", "https://shorturl.at/gjQZ7"),
    Song("American Wedding", "nostalgia, ULTRA", "https://shorturl.at/AJOV1"),
    Song("Swim Good", "nostalgia, ULTRA", "https://open.spotify.com/track/3CgZCQyuyxHRMWB9BTwmni?si=ab2a56b458eb46ba"),

    # Channel Orange
    Song("Thinkin Bout You", "Channel Orange", "https://open.spotify.com/track/7DfFc7a6Rwfi3YQMRbDMau?si=dd6b7bc6e83b49d5"),
    Song("Sierra Leone", "Channel Orange", "https://open.spotify.com/track/1HwbgJAU9PZ7YbzKgVgoIF?si=dd29dfb02f604488"),
    Song("Sweet Life", "Channel Orange", "https://open.spotify.com/track/6MEDfjHxnVNcYmHe3mM6L2?si=dbde93706c9b430d"),
    Song("Super Rich Kids", "Channel Orange", "https://open.spotify.com/track/0725YWm6Z0TpZ6wrNk64Eb?si=8d6ca1c7585e43ac"),
    Song("Pilot Jones", "Channel Orange", "https://open.spotify.com/track/2ohegz9maxzroKBu9YhcCM?si=284e2172ed3b4daf"),
    Song("Crack Rock", "Channel Orange", "https://open.spotify.com/track/5lcyIeEfwZTs8Ajw3kdF7P?si=4407d42209f44f9a"),
    Song("Pyramids", "Channel Orange", "https://open.spotify.com/track/4QhWbupniDd44EDtnh2bFJ?si=98cd631ea7654d4c"),
    Song("Lost", "Channel Orange", "https://open.spotify.com/track/3GZD6HmiNUhxXYf8Gch723?si=bf57e04e12c94655"),
    Song("Monks", "Channel Orange", "https://open.spotify.com/track/0msrDPXxZpts4FRnoX0bFr?si=cd0cfe278e2e49eb"),
    Song("Bad Religion", "Channel Orange", "https://open.spotify.com/track/2pMPWE7PJH1PizfgGRMnR9?si=48399a0fbdbc4b79"),
    Song("Pink Matter", "Channel Orange", "https://open.spotify.com/track/1fOkmYW3ZFkkjIdOZSf596?si=19c94a9950e3406f"),
    Song("Forrest Gump", "Channel Orange", "https://open.spotify.com/track/4YZbVct8l9MnAVIROnLQdx?si=3314d6f9ccfb44a9"),
    Song("Golden Girl", "Channel Orange", "https://www.youtube.com/watch?v=zkggNyE5ZoA"),

    # Endless
    Song("At Your Best (You Are Love)", "ENDLESS", "https://shorturl.at/dgkB5"),
    Song("Alabama", "ENDLESS", "https://shorturl.at/mzJV7"),
    Song("U-N-I-T-Y", "ENDLESS", "https://shorturl.at/irUW6"),
    Song("Comme Des Garcons", "ENDLESS", "https://shorturl.at/fhJY3"),
    Song("Xenons", "ENDLESS", "https://www.youtube.com/watch?v=PrbGgcAaHlA"),
    Song("Wither", "ENDLESS", "https://www.youtube.com/watch?v=FTbX0OPdIL0"),
    Song("Hublots", "ENDLESS", "https://shorturl.at/BCPS1"),
    Song("In Here Somewhere", "ENDLESS", "https://shorturl.at/fjLP9"),
    Song("Slide on Me", "ENDLESS", "https://shorturl.at/fsw46"),
    Song("Sideways", "ENDLESS", "https://shorturl.at/GQVZ6"),
    Song("Florida", "ENDLESS", "https://shorturl.at/EQT14"),
    Song("Rushes", "ENDLESS", "https://shorturl.at/rwAY4"),
    Song("Rushes To", "ENDLESS", "https://shorturl.at/a1235"),
    Song("Higgs", "ENDLESS", "https://shorturl.at/cjKYZ"),
    Song("Mitsubishi Sony", "ENDLESS", "https://shorturl.at/orR34"),

    # Blonde
    Song("Nikes", "Blonde", "https://open.spotify.com/track/19YKaevk2bce4odJkP5L22?si=9b042d895aef4546"),
    Song("Ivy", "Blonde", "https://open.spotify.com/track/2ZWlPOoWh0626oTaHrnl2a?si=f0817446ecb047bc"),
    Song("Pink + White", "Blonde", "https://open.spotify.com/track/3xKsf9qdS1CyvXSMEid6g8?si=abd27088142a42a7"),
    Song("Solo", "Blonde", "https://open.spotify.com/track/35xSkNIXi504fcEwz9USRB?si=9ba33ae85a1046fa"),
    Song("Skyline To", "Blonde", "https://open.spotify.com/track/4xR3MAscflQ262kMeiKshQ?si=479bc5cfeb6442dd"),
    Song("Good Guy", "Blonde", "https://open.spotify.com/track/2JUqYobT8NvARdPmc4ES2x?si=d7f68d8161ac47df"),
    Song("Nights", "Blonde", "https://open.spotify.com/track/7eqoqGkKwgOaWNNHx90uEZ?si=d1a15521fa2f45ce"),
    Song("Solo (Reprise)", "Blonde", "https://open.spotify.com/track/2qtoRFCOEL1gRn5q9DJC7F?si=caccda2e894a469a"),
    Song("Pretty Sweet", "Blonde", "https://open.spotify.com/track/17yrCsl1Ai6CZLBmGj6d6p?si=d79566a1242c4fe8"),
    Song("Close to You", "Blonde", "https://open.spotify.com/track/1VZLEW5ZfcAbKZ94XQiSZF?si=a8f340d0a84e49d3"),
    Song("White Ferrari", "Blonde", "https://open.spotify.com/track/2LMkwUfqC6S6s6qDVlEuzV?si=c9827e4208b54a6f"),
    Song("Seigfried", "Blonde", "https://open.spotify.com/track/1BViPjTT585XAhkUUrkts0?si=995e1e5873cb4f71"),
    Song("Godspeed", "Blonde", "https://open.spotify.com/track/34xTFwjPQ1dC6uJmleno7x?si=8e01b39f3dc94bc0"),
    Song("Futura Free", "Blonde", "https://open.spotify.com/track/5k8LB57xOq8UUNVaKWSqrf?si=ac3b0f62899d4f6b"),

    # Features and Singles
    Song("Dear April", "Single", "https://open.spotify.com/track/62ljuuXo0zrcrtJnnOhfxT?si=6b4855c4db934631"),
    Song("Cayendo", "Single", "https://open.spotify.com/track/72794Eag03xdy7TO0KNuid?si=6ace172fb92e4348"),
    Song("In My Room", "Single", "https://open.spotify.com/track/4S4Mfvv03M1cHgIOJcbUCL?si=51c3eb1dcf9340c2"),
    Song("DHL", "Single", "https://open.spotify.com/track/2INhKpUdzh7v0j041gZNsz?si=f17a61412ee341f0"),
    Song("Moon River", "Single", "https://open.spotify.com/track/41cpvQ2GyGb2BRdIRSsTqK?si=a7b0d5c1845847b9"),
    Song("Provider", "Single", "https://open.spotify.com/track/6R6ihJhRbgu7JxJKIbW57w?si=c69af0f035f24396"),
    Song("Biking (Solo)", "Single", "https://open.spotify.com/track/6gtNiLJNLBcV0P6Juenstp?si=edcedeb1121b4ccc"),
    Song("Lens", "Single", "https://open.spotify.com/track/371H6HjS4SXGbQ9IVfFUIL?si=dca95311161f4626"),
    Song("Biking", "Single", "https://open.spotify.com/track/2q0VexHJirnUPnEOhr2DxK?si=cd2228a1a0c3404c"),
    Song("Chanel", "Single", "https://open.spotify.com/track/6Nle9hKrkL1wQpwNfEkxjh?si=d90ed6dbecc14695"),
    Song("Memrise", "Single", "https://www.youtube.com/watch?v=M3Soy9tSlTM"),
    Song("Wiseman", "Single", "https://www.youtube.com/watch?v=HTemWSAttUM"),
]
