#love like you, by rebecca sugar, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_lovelikeyou",
            category=[mas_songs.TYPE_LONG],
            prompt="Love Like You",
            random=True
        ),
        code="SNG"
    )

label otter_song_lovelikeyou:
    m "{i}~If I could begin to be~{/i}"
    m "{i}~Half of what you think of me~{/i}"
    m "{i}~I could do about anything~{/i}"
    m "{i}~I could even learn how to love~{/i}"
    m "{i}~When I see the way you act~{/i}"
    m "{i}~Wondering when I'm coming back~{/i}"
    m "{i}~I could do about anything~{/i}"
    m "{i}~I could even learn how to love ~{/i}"
    extend "{i}like you~{/i}"
    m "{i}~I always thought I might be bad~{/i}"
    m "{i}~Now I’m sure that it's true~{/i}"
    m "{i}~‘Cause I think you’re so good~{/i}"
    m "{i}~And I’m nothing like you~{/i}"
    m "{i}~Look at you go~{/i}"
    m "{i}~I just adore you~{/i}"
    m "{i}~I wish that I knew~{/i}"
    m "{i}~What makes you think I'm so special~{/i}"
    m "{i}~If I could begin to do~{/i}"
    m "{i}~Something that does right by you~{/i}"
    m "{i}~I would do about anything~{/i}"
    m "{i}~I would even learn how to love~{/i}"
    m "{i}~When I see the way you look~{/i}"
    m "{i}~Shaken by how long it took~{/i}"
    m "{i}~I could do about anything~{/i}"
    m "{i}~I could even learn how to love like you~{/i}"
    m "..."
    return
