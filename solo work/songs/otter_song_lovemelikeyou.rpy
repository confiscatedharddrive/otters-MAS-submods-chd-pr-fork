#love me like you, by little mix, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_lovemelikeyou",
            conditional="mas_isMoniNormal(higher=True)",
            category=[mas_songs.TYPE_SHORT],
            prompt="Love Me Like You",
            action=EV_ACT_RANDOM
        ),
        code="SNG"
    )

label otter_song_lovemelikeyou:
    m "{i}~So baby, baby~{/i}"
    m "{i}~Come and save me~{/i}"
    m "{i}~Don’t need those other numbers~{/i}"
    m "{i}~When I got my number one~{/i}"
    m "{i}~Last night I lay in bed so blue~{/i}"
    m "{i}~'Cause I realised the truth~{/i}"
    m "{i}~They can’t love me like you~{/i}"
    m "{i}~I tried to find somebody new~{/i}"
    m "{i}~Baby, they ain’t got a clue~{/i}"
    m "{i}~Can’t love me like you~{/i}"
    m "..."
    m "No one can love me like you do, [player]."
    m "And I love you more than anything in the world!"
    m "Thank you for being mine, [mas_get_player_nickname()]."
    return "love"
    
#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
