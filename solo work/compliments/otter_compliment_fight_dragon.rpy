#If we were in the Middle Ages, I’d fight a dragon for you.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_otter_compliment_fight_dragon",
            prompt="If we were in the Middle Ages, I’d fight a dragon for you.",
            unlocked=True
        ),
        code="CMP"
    )

label monika_otter_compliment_fight_dragon:
    m 1tsbfb "Aww, is that right, my dragon slayer?"
    m "I love you so much!"
    m "No creature would scare me if you were in danger!"
    m 4tsbfb "I would fight basilisks, manticores, cerberus..."
    m 3ssbfu "If that would mean being by your side!"
    m 5fkbfa "My medieval hero."
    return
