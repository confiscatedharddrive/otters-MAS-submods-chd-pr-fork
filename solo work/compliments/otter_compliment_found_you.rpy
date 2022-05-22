#I can’t believe I found someone like you.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_found_you",
            prompt="I can’t believe I found someone like you.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_found_you:
    m ""
    return
