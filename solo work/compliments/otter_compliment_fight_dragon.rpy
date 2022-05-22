#If we were in the Middle Ages, I’d fight a dragon for you.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_fight_dragon",
            prompt="If we were in the Middle Ages, I’d fight a dragon for you.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_fight_dragon:
    m ""
    return
