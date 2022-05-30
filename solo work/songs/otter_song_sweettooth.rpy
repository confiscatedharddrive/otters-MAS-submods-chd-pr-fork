#sweet tooth, by cavetown, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_sweettooth",
            category=[mas_songs.TYPE_SHORT],
            prompt="Sweet Tooth",
            random=True
        ),
        code="SNG"
    )

label otter_song_sweettooth:
    m "{i}~You said you love me exactly the way I am~{/i}"
    m "{i}~And you know I find it hard to understand~{/i}"
    m "{i}~Pay a visit to the doctor 'cause I have~{/i}"
    m "{i}~A sweet tooth for you~{/i}"
    m "{i}~I'm wide awake~{/i}"
    m "{i}~The sugar went straight to my brain~{/i}"
    m "{i}~Feel like a kid, I double tap~{/i}"
    m "{i}~My chest with my fist~{/i}"
    m "{i}~I like you~{/i}"
    m "{i}~Say it back~{/i}"
    m "{i}~Never had a cavity~{/i}"
    m "{i}~Never had nobody as sweet as you~{/i}"
    m "..."
    return

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
