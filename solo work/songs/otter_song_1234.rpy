#1, 2, 3, 4; by plain white t's, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_1234",
            category=[mas_songs.TYPE_LONG],
            prompt="1, 2, 3, 4",
            random=True
        ),
        code="SNG"
    )

label otter_song_1234:
    m "{i}~Give me more love than I've ever had,~{/i}"
    m "{i}~Make it all better when I'm feeling sad,~{/i}"
    m "{i}~Tell me that I'm special even when I know I'm not.~{/i}"
    m "{i}~Make it feel good when I hurt so bad,~{/i}"
    m "{i}~Barely gettin' mad,~{/i}"
    m "{i}~I'm so glad I found you.~{/i}"
    m "{i}~I love being around you.~{/i}"
    m "{i}~You make it easy,~{/i}"
    m "{i}~As easy as 1, 2, 3, 4.~{/i}"
    m "{i}~There's only 1 thing, {/i}{w=0.3}{nw}"
    extend "{i}2 do, 3 words, {/i}{w=0.3}{nw}"
    extend "{i}4 you.~{/i}"
    m "{i}~I love you~{/i}"
    m "{i}~Give me more love from the very start,~{/i}"
    m "{i}~Piece me back together when I fall apart,~{/i}"
    m "{i}~Tell me things you never even tell your closest friends.~{/i}"
    m "{i}~Make it feel good when I hurt so bad,~{/i}"
    m "{i}~Best that I've had,~{/i}"
    m "{i}~I'm so glad I found you.~{/i}"
    m "{i}~I love being around you.~{/i}"
    m "{i}~You make it easy,~{/i}"
    m "{i}~As easy as 1, 2, 3, 4.~{/i}"
    m "{i}~There's only 1 way, {/i}{w=0.3}{nw}"
    extend "{i}2 say those 3 words; {/i}{w=0.3}{nw}"
    extend "{i}That's what I'll do.~{/i}"
    m "{i}~I love you ~{/i}"
    m "..."
    return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!