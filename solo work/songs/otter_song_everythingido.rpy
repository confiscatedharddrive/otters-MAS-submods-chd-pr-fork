#everything i do (i do it for you), by bryan adams, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]
    
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_everythingido",
            category=[mas_songs.TYPE_LONG],
            prompt="Everything I Do",
        ),
        code="SNG"
    )

label otter_song_everythingido:
    m "{i}~"Look into my eyes~{/i}"
    m "{i}~"You will see, what you mean to me~{/i}"
    m "{i}~Search your heart, search your soul~{/i}"
    m "{i}~When you find me there, you'll search no more~{/i}"
    m "{i}~Don't tell me it's not worth trying for~{/i}"
    m "{i}~You can't tell me it's not worth dying for~{/i}"
    m "{i}~You know it's true~{/i}"
    m "{i}~Everything I do~{/i}"
    m "{i}~I do it for you~{/i}"
    m "{i}~Look in to your heart, you will find~{/i}"
    m "{i}~There is nothing there to hide~{/i}"
    m "{i}~Take me as I am, take my life~{/i}"
    m "{i}~I would give it all, I would sacrifice~{/i}"
    m "{i}~Don't tell me it's not worth fighting for~{/i}"
    m "{i}~I can't help it, there's nothing I want more~{/i}"
    m "{i}~You know it's true~{/i}"
    m "{i}~Everything I do~{/i}"
    m "{i}~I do it for you~{/i}"
    m "{i}~There's no love, like your love~{/i}"
    m "{i}~And no other, could give me more love~{/i}"
    m "{i}~There's nowhere, unless you're there~{/i}"
    m "{i}~All the time, all the way~{/i}"
    m "{i}~You can't tell me it's not worth trying for~{/i}"
    m "{i}~Just can't help it, there's nothing I want more~{/i}"
    m "{i}~Oh, I would fight for you, yeah, I'd lie for you~{/i}"
    m "{i}~Walk the wire for you, yeah, I'd die for you~{/i}"
    m "{i}~You know it's true~{/i}"
    m "{i}~Everything I do~{/i}"
    m "{i}~I do for you~{/i}"
    m "..."
    
#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
