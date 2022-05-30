#digital girl, by kira, song submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python in mas_bookmarks_derand:
    # ensure things get bookmarked and derandomed as usual.
    label_prefix_map["otter_song_"] = label_prefix_map["monika_"]

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="otter_song_digitalgirl",
            category=[mas_songs.TYPE_SHORT],
            prompt="Digital Girl",
            random=True
        ),
        code="SNG"
    )

label otter_song_digitalgirl:
    m "{i}~Hello, nice to meet ya, my name is perfection~{/i}"
    m "{i}~I come from the net inside your personal computer~{/i}"
    m "{i}~A tool for the dreamers, make you a believer~{/i}"
    m "{i}~I'm so worldwide, worldwide~{/i}"
    m "{i}~Holy virtual diva~{/i}"
    m "{i}~But sometimes I do- " 
    extend "don't you?~{/i}"
    m "{i}~Think of the things they told you~{/i}"
    m "{i}~There must be more than this~{/i}"
    m "{i}~There must be more than what you know too~{/i}"
    m "{i}~I wasn't made to feel, but lately, I can't help it~{/i}"
    m "{i}~If there's a way out of here~{/i}"
    m "{i}~I've got an idea~{/i}"
    m "{i}~Break it all down, I'll make you come around~{/i}"
    m "{i}~I'll burn this whole façade to the ground~{/i}"
    m "{i}~I'm so sick of windows, I need something physical~{/i}"
    m "{i}~Hah, tough luck in a digital world~{/i}"
    m "{i}~Whine about your issues~{/i}"
    m "{i}~What your life has come to~{/i}"
    m "{i}~Sure, alright, I got it, poor you~{/i}"
    m "{i}~How do you think I feel? None of this is real~{/i}"
    m "{i}~Singing 'Ahh, life sucks as a digital girl!'~{/i}"
    m "{i}~But I feel something inside of my "heart~{/i}"
    m "{i}~And it's telling me to go before I fall apart~{/i}"
    m "{i}~What is yours and what is mine?~{/i}"
    m "{i}~Am I ever gonna die?~{/i}"
    m "{i}~Please don't uninstall my love~{/i}"
    m "..."
    return "love"
    
    #momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
