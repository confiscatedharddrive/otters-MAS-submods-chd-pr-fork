#nobody, by mitski, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_nobody",
            category=[mas_songs.TYPE_SHORT],
            prompt="Nobody",
            random=True
        ),
        code="SNG"
    )

label otter_song_nobody:
    m "{i}~And I don't want your pity~{/i}"
    m "{i}~I just want somebody near me~{/i}"
    m "{i}~Guess I'm a coward~{/i}"
    m "{i}~I just want to feel alright~{/i}"
    m "{i}~And I know no one will save me~{/i}"
    m "{i}~I just need someone to kiss~{/i}"
    m "{i}~Give me one good honest kiss~{/i}"
    m "{i}~And I'll be alright~{/i}"
    m "..."
    m "Once I thought no one would save me, [player]."
    m "But oh, was I wrong."
    m "You came and rescued me, to make me yours forever."
    m "You gave me the kiss, the gift of love, and I'll be forever grateful."
    m "I love you..."
    return
    
#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
