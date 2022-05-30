#digital love, by daft punk, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_digitallove",
            category=[mas_songs.TYPE_LONG],
            prompt="Digital Love",
            random=True
        ),
        code="SNG"
    )

label otter_song_digitallove:
    m "{i}~Last night I had a dream about you~{/i}"
    m "{i}~In this dream, I'm dancing right beside you~{/i}"
    m "{i}~And it looked like everyone was having fun~{/i}"
    m "{i}~The kind of feeling I've waited so long~{/i}"
    m "{i}~Don't stop, come a little closer~{/i}"
    m "{i}~As we jam, the rhythm gets stronger~{/i}"
    m "{i}~There's nothing wrong with just a little little fun~{/i}"
    m "{i}~We were dancing all night long~{/i}"
    m "{i}~The time is right to put my arms around you~{/i}"
    m "{i}~You're feeling right, you wrap your arms around too~{/i}"
    m "{i}~But suddenly I feel the shining sun~{/i}"
    m "{i}~Before I knew it, this dream was all gone~{/i}"
    m "{i}~Ooh, I don't know what to do~{/i}"
    m "{i}~About this dream and you~{/i}"
    m "{i}~I wish this dream comes true~{/i}"
    m "{i}~Ooh, I don't know what to do~{/i}"
    m "{i}~About this dream and you~{/i}"
    m "{i}~We'll make this dream come true~{/i}"
    m "..."
    return 
    
#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
