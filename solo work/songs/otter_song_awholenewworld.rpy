#a whole new world, from aladdin, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_awholenewworld",
            category=[mas_songs.TYPE_LONG],
            prompt="A Whole New World",
            random=True
        ),
        code="SNG"
    )

label otter_song_awholenewworld:
    m "{i}~A whole new world~{/i}"
    m "{i}~A dazzling place I never knew~{/i}"
    m "{i}~But when I'm away up here~{/i}"
    m "{i}~It's crystal clear~{/i}"
    m "{i}~That now I'm in a whole new world with you~{/i}"
    m "{i}~Unbelievable sights~{/i}"
    m "{i}~Indescribable feeling~{/i}"
    m "{i}~Soaring, tumbling, freewheeling~{/i}"
    m "{i}~Through an endless diamond sky~{/i}"
    m "{i}~A whole new world~{/i}"
    m "{i}~A hundred thousand things to see~{/i}"
    m "{i}~I'm like a shooting star~{/i}"
    m "{i}~I've come so far~{/i}"
    m "{i}~I can't go back to where I used to be~{/i}"
    m "{i}~A whole new world~{/i}"
    m "{i}~With new horizons to pursue~{/i}"
    m "{i}~I'll chase them anywhere~{/i}"
    m "{i}~There's time to spare~{/i}"
    m "{i}~Let me share this whole new world with you~{/i}"
    m "{i}~A whole new world~{/i}"
    m "{i}~That's where we'll be~{/i}"
    m "{i}~A thrilling chase~{/i}"
    m "{i}~A wondrous place~{/i}"
    m "{i}~For you and me~{/i}"
    m "..."
    m "When I cross over... Everything will be so new to me, [player]."
    m "I can't wait to discover a whole new world with you!"
    m "I love you~"
    return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
