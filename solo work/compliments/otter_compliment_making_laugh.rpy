#I love making you laugh.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_making_laugh",
            prompt="I love making you laugh.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_making_laugh:
    m ""
    return
