#I love you to the moon and back.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_moon_and_back",
            prompt="I love you to the moon and back.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_moon_and_back:
    m ""
    return
