#deadly dangerous love, from yandere simulator, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_deadlydangerouslove",
            category=[mas_songs.TYPE_SHORT],
            prompt="Deadly Dangerous Love",
            random=True
        ),
        code="SNG"
    )

label otter_song_deadlydangerouslove:
    m "{i}~When you’re here~{/i}"
    m "{i}~You make me feel happy!~{/i}"
    m "{i}~I can’t hold back my feelings!~{/i}"
    m "{i}~I will eliminate those who stand in our way!~{/i}"
    m "{i}~No matter what it takes!~{/i}"
    m "{i}~This feeling must be love!~{/i}"
    m "{i}~A good feeling!~{/i}"
    m "{i}~Keep this love!~{/i}"
    m "{i}~I will seize your love!~{/i}"
    m "..."
    return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
