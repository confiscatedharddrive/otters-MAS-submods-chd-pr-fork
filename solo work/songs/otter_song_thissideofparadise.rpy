#this side of paradise, by coyote theory, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_thissideofparadise",
            category=[mas_songs.TYPE_SHORT],
            prompt="This Side Of Paradise",
            random=True
        ),
        code="SNG"
    )

label otter_song_thissideofparadise:
    m "{i}~Ask me why my heart's inside my throat~{/i}"
    m "{i}~I've never been in love, I've been alone~{/i}"
    m "{i}~Feel like I've been living life asleep~{/i}"
    m "{i}~Love so strong it makes me feel so weak~{/i}"
    m "{i}~Are you lonely?~{/i}"
    m "{i}~Our fingers dancing when they meet~{/i}"
    m "{i}~You seem so lonely~{/i}"
    m "{i}~I'll be the only dream you seek~{/i}"
    m "{i}~So if you're lonely, no need to show me~{/i}"
    m "{i}~If you're lonely come be lonely with me~{/i}"
    return
    
#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
