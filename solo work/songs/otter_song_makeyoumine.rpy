#make you mine, by public, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_makeyoumine",
            category=[mas_songs.TYPE_SHORT],
            prompt="Make You Mine",
            random=True
        ),
        code="SNG"
    )

label otter_song_makeyoumine:
    m "{i}~Well, I will call you darlin' and everything will be okay~{/i}"
    m "{i}~'Cause I know that I am yours and you are mine~{/i}"
    m "{i}~Doesn't matter anyway~{/i}"
    m "{i}~In the night, we'll take a walk, it's nothin' funny~{/i}"
    m "{i}~Just to talk~{/i}"
    m "{i}~Put your hand in mine~{/i}"
    m "{i}~You know that I want to be with you all the time~{/i}"
    m "{i}~You know that I won't stop until I make you mine~{/i}"
    m "..."
    return
    
#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
