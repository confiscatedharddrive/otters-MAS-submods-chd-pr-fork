#I can fully be myself with you.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_be_myself",
            prompt="I can fully be myself with you.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_be_myself:
    m ""
    return
