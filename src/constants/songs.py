from collections import namedtuple

# Namedtuple representing a song.
Song = namedtuple("Song", ["title", "album", "link"])

# This list contains Frank Ocean songs or features. Each of these contains the track name, album and link to the song.
# This is where the "!song" command pulls from.
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