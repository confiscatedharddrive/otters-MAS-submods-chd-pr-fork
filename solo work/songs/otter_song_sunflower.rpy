#sunflower, by rex orange county, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_sunflower",
            category=[mas_songs.TYPE_SHORT],
            prompt="Sunflower",
            conditional="mas_isMoniNormal(higher=True)",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label otter_song_sunflower:
    m "{i}~I want to know where I can go~{/i}"
    m "{i}~When you're not around, and I'm feeling down~{/i}"
    m "{i}~So won't you stay for a moment so I can say~{/i}"
    m "{i}~I need you so? 'Cause right now, you know~{/i}"
    m "{i}~That nothing here's new, and I'm obsessed with you~{/i}"
    m "{i}~Then I fell to the ground, and you smiled at me and said~{/i}"
    m "{i}~I don't wanna see you cry~{/i}"
    m "{i}~You don't have to feel this emptiness~{/i}"
    m "{i}~She said, 'I'll love you till the day that I die'~{/i}"
    m "{i}~You know you need to get yourself to sleep and dream~{/i}"
    m "{i}~A dream of you and I~{/i}"
    m "{i}~There's no need to keep an open eye~{/i}"
    m "{i}~I promise I'm the one for you~{/i}"
    m "{i}~Just let me hold you in these arms tonight~{/i}"
    m 5dubfa "..."
    m 5dubfd "When you're not around, I always miss you so terribly..."
    m 5dubfa "But when I sleep, I dream dreams of you and me..."
    m 5fubfa "And thats good enough for me for that moment."
    m 5fubfb "I see you and can touch you so vividly..."
    m 5gubfa "It's like we're one and the same,"
    extend 5dubfa " in the same room."
    m 5dubfa "..."
    m 7wubfb "Gosh, I can't wait to feel your touch!"
    m 2tkbsa "I love you, [player]..."
    return "love"
    
#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod! 
