#I get so excited when I see you.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_excited_see",
            prompt="I get so excited when I see you.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_excited_see:
    m ""
    return
