#I'm going to stretch my legs, brb submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_stretch",
            category=["be right back"],
            prompt="I'm going to stretch my legs",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_stretch:
    m 1wud "Your body needs some rest, [player]?"
    m 3hua "No problem! I'll be waiting here for you."
    m 3dub "Take your time, maybe stretch a little bit or lie down."
    m 1hub "Whatever you need!"
    m 1kua "See you in a bit~"

$ mas_idle_mailbox.send_idle_cb("otter_brb_stretch_callback")
return "idle"

label otter_brb_stretch_callback:
    m 3wub "Welcome back, [player]!"
    m 1dua "I hope your body feels more rested now~"
    m 1kua "Let's spend more time together!"

return

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
