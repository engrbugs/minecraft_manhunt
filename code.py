# millisecond

def on_on_chat():
    while True:
        player.say("catch me if you can!")
        mypos = player.position()
        player.say(mypos)
        loops.pause(60000)
player.on_chat("man_hunt", on_on_chat)
