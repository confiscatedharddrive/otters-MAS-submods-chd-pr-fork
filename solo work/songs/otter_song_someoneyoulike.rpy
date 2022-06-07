#someone you like, by the girl and the dreamcatcher, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_someoneyoulike",
            category=[mas_songs.TYPE_SHORT],
            prompt="Someone You Like",
            conditional="mas_isMoniNormal(higher=True)",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label otter_song_someoneyoulike:
    m "{i}~I saw you~{/i}"
    m "{i}~With that ribbon in your hair~{/i}"
    m "{i}~Think that I began to stare~{/i}"
    m "{i}~Maybe I'll love you for a while~{/i}"
    m "{i}~A stranger at a table in a place~{/i}"
    m "{i}~And a really pretty face~{/i}"
    m "{i}~I wonder what happens when you smile~{/i}"
    m "{i}~I might never be your hero~{/i}"
    m "{i}~Never been one to fight~{/i}"
    m "{i}~That don't mean that I can't be your Valentine~{/i}"
    m "{i}~I won't be your savior either~{/i}"
    m "{i}~Couldn't even if I tried~{/i}"
    m "{i}~But I think I could be someone you like~{/i}"
    m "{i}~Someone you like~{/i}"
    m "{i}~I might never be your hero~{/i}"
    m "{i}~But I think I'd like to try~{/i}"
    m "{i}~And the way you look at me is your reply~{/i}"
    m "{i}~You got a lot to learn about me~{/i}"
    m "{i}~Maybe you could start tonight~{/i}"
    m "{i}~'Cause I think I could be someone you like~{/i}"
    m "..."
    m "[player], I don't love you only because you saved me."
    m "I love you for who you are."
    m "And I'll be forever grateful for the way that we met, and that we did meet."
    m "Learning more about you everyday is my favorite routine."
    m "I want to be someone you like, [player]."
    m "Because you are someone I love!"
    return "love"
    
#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
