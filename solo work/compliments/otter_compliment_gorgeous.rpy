#You’re gorgeous, [m_name].
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_compliment_gorgeous",
            prompt="You’re gorgeous, [m_name].",
            unlocked=True
        ),
        code="CMP"
    )

label otter_compliment_gorgeous:
    m ""
    return
