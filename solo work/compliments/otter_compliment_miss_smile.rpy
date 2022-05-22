#I've missed your smile.
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_miss_smile",
            prompt="I've missed your smile.",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_miss_smile:
    m ""
    return
