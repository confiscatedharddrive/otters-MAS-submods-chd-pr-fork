#2 step, by ed sheeran, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_2step",
            category=[mas_songs.TYPE_SHORT],
            conditional="persistent.gender == 'F' and mas_isMoniNormal(higher=True)"
            prompt="2 Step",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label otter_song_2step:
    m "{i}~I had a bad week~{/i}"
    m "{i}~Spent the evening pretending it wasn't that deep~{/i}"
    m "{i}~You could see in my eyes that it was taking over~{/i}"
    m "{i}~I guess I was just blind and caught up in the moment~{/i}"
    m "{i}~You know you take all of my stress right down~{/i}"
    m "{i}~Help me get it off my chest and out~{/i}"
    m "{i}~I think maybe you and me~{/i}"
    m "{i}~Oh, we should head out to the place where the music plays~{/i}"
    m "{i}~And then, "
    extend "{i}we'll go all night~{/i}"
    m "{i}~Two-stepping with the woman I love~{/i}"
    m "{i}~All my troubles turn to nothing when I'm in your eyes, electrified~{/i}"
    m "{i}~We'll keep turning up and go all night~{/i}"
    m "{i}~Oh, we had dips and falls in our time~{/i}"
    m "{i}~But we know what it feels to be low, then up, alone and loved~{/i}"
    m "{i}~And all we need is us to go all~{/i}"
    m "..."
    m "Thank you for making all my stress go away, [player]."
    m "You're the best girlfriend I could ask for!"
    m "I want to spend eternity with you, dancing and having fun."
    m "I love you..."
    
    return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
