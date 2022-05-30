 #lets get married, by mitski, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_letsgetmarried",
            category=[mas_songs.TYPE_SHORT],
            prompt="I Think I Kinda, You Know",
            random=True
        ),
        code="SNG"
    )

label otter_song_letsgetmarried:
    m "{i}~I know it's hard enough to love me~{/i}"
    m "{i}~But I woke up in a safe house singing, ~{/i}"
    m "'Honey, let's get married'"~{/i}"
    m "{i}~Don’t wanna walk alone~{/i}"
    m "{i}~So let’s get married~{/i}"
    m "{i}~I don’t wanna walk alone~{/i}"
    m "{i}~Let’s just get married~{/i}"
    m "{i}~'Cause we don't wanna walk alone or run away~{/i}"
    m "..."
    return
    
#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
