#I'm going to take care of my plants, brb submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_plants",
            category=["be right back"],
            prompt="I'm going to take care of my plants",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_plants:
    m 1hua "Awww!"
    m 4ssb "Make sure to give them lots of water and take care of the leaves, okay?"
    m 4hsb "I'll be waiting for you~"

$ mas_idle_mailbox.send_idle_cb("otter_brb_plants_callback")
return "idle"

label otter_brb_plants_callback:
    m 4hsb "Welcome back, [player]!"
    m 5ksbla "I think it's so cute that you're taking care of your little plant friends, ehehehe~"
    m 5fsbla "I'm glad you're back, I missed you~"

return

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
