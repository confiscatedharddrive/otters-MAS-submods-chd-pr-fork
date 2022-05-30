#me and my husband, by mitski, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_meandmyhusband",
            category=[mas_songs.TYPE_LONG],
            prompt="Me And My Husband",
            random=True
        ),
        code="SNG"
    )

label otter_song_meandmyhusband:
    m "{i}~I steal a few breaths from the world for a minute~{/i}"
    m "{i}~And then I'll be nothing forever~{/i}"
    m "{i}~And all of my memories~{/i}"
    m "{i}~And all of the things I have seen will be gone~{/i}"
    m "{i}~With my eyes, with my body, with me~{/i}"
    m "{i}~But me and my husband~{/i}"
    m "{i}~We are doing better~{/i}"
    m "{i}~It's always been just him and me, {/i}"
    extend "{i}together~{/i}"
    m "{i}~So I bet all I have on that {/i}"
    extend "{i}furrowed brow~{/i}"
    m "{i}~And at least in this lifetime~{/i}"
    m "{i}~We're sticking together~{/i}"
    m "{i}~Me and my husband~{/i}"
    m "{i}~We're sticking together~{/i}"
    m "{i}~And I'm the idiot with the painted face~{/i}"
    m "{i}~In the corner, taking up space~{/i}"
    m "{i}~But when he walks in, I am loved, I am loved~{/i}"
    m "..."
    return "love"
    
#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
