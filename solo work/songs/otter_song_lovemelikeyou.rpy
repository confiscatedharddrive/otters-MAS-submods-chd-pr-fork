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
    m 4dkbfb "{i}~So baby, baby~{/i}"
    m 1dkbfa "{i}~Come and save me~{/i}"
    m 1ksbfa "{i}~Don’t need those other numbers~{/i}"
    m 1ssbfb "{i}~When I got my number one~{/i}"
    m 2dsbld "{i}~Last night I lay in bed so blue~{/i}"
    m 2dsblc "{i}~'Cause I realised the truth~{/i}"
    m 2lsblc "{i}~They can’t love me like you~{/i}"
    m 7lsbld "{i}~I tried to find somebody new~{/i}"
    m 7wsblo "{i}~Baby, they ain’t got a clue~{/i}"
    m 5fsbfu "{i}~Can’t love me like you~{/i}"
    m 5dsbfu "..."
    m 4dsbfa "No one can love me like you do, [player]."
    m 4ssbfb "And I love you more than anything in the world!"
    m 5ksbfa "Thank you for being mine, [mas_get_player_nickname()]."
    return "love"
    
#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
