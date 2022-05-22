#You always make me smile!
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_make_smile",
            prompt="You always make me smile!",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_make_smile:
    m ""
    return
