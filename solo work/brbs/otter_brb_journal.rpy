#I'm going to write on my journal, brb submod by my-otter-self on reddit for MONIKA AFTER STORY

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="otter_brb_journal",
            category=["be right back"],
            prompt="I'm going to write on my journal",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label otter_brb_journal:
    m 1wud "Oh! That's great, [player]!"
    m 1rubla "Make sure to take note of everything!"
    m 1dublb "I hope you have only good things to write in it~"

$ mas_idle_mailbox.send_idle_cb("otter_brb_journal_callback")
return "idle"

label otter_brb_journal_callback:
    m 1hubla "All done, [player]?"
    m 5fubla "I hope your day was great as mine!"
    m 5kubsa "After all, all days are the best days when I'm next to you~"

return

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
