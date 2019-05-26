"""
An example file demonstrating how to use the chatlog.
"""

# Copyright 2019 John-Michael O'Brien
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Date Created: 5/25/2019

# IM
define audio.im = "sounds/im.mp3"
# Tapping
define audio.tapping = "sounds/tapping.mp3"
# Pocket Insert
define audio.pocket_insert = "sounds/pocket insert.mp3"
# Pocket Remove
define audio.pocket_remove = "sounds/pocket remove.mp3"

screen sms():
    frame id "phone_screen":
        xpos 120
        ypos 10
        xsize 1040
        ysize 500
        padding Borders(70,80,72,72).padding
        background Frame("phone_frame.png", 70, 80, 72, 72, tile=False)
        foreground None

        use chat_log(msgs)

label start:
    default msgs = ChatLog()

    scene bg room

    "It's too early to get up."

    play sound im

    "Hmm?"

    $ msgs.add_chat(msg="Hello Marcy!", nick="Bubba", avatar="chat.png")

    play sound pocket_remove
    show screen sms with Dissolve(1.0)

    "Oooh! A text!"

    play sound tapping
    "I should write back!"

    "And send!"

    play sound im
    $ msgs.add_chat(msg="Hiya Bubba!", nick="Marcy", avatar="chat2.png")

    "Yay! I'm talking!"

    play sound im
    $ msgs.add_chat(msg="So yesterday I did a thing.", nick="Bubba", avatar="chat.png")

    "Neat!"

    play sound im
    $ msgs.add_chat(msg="And I ended up making a bunch of cake!", nick="Bubba", avatar="chat.png")

    pause 1

    play sound im
    $ msgs.add_chat(msg="It is a chocolate raspberry cake.", nick="Bubba", avatar="chat.png")

    pause 1

    play sound im
    $ msgs.add_chat(msg="My boyfriend hates it.", nick="Bubba", avatar="chat.png")

    pause 0.5

    play sound im
    $ msgs.add_chat(msg="But I love the color.", nick="Bubba", avatar="chat.png")

    pause 0.3

    play sound im
    $ msgs.add_chat(msg="And the smell.", nick="Bubba", avatar="chat.png")

    pause 0.3

    play sound im
    $ msgs.add_chat(msg="And the taste!", nick="Bubba", avatar="chat.png")

    "Geez! Too much chat!"

    play sound im
    $ msgs.add_chat(msg="You still there?", nick="Bubba", avatar="chat.png")

    ".{w=1}.{w=1}.{w=1}"

    play sound tapping
    "Nope. Time to bail."

    play sound im
    $ msgs.add_chat(type="chat_picture", pic="no.jpg", nick="Marcy", avatar="chat2.png")

    pause 1

    play sound im
    $ msgs.add_chat(msg="G2G. TTYL!", nick="Marcy", avatar="chat2.png")

    "Time to put the phone away."
    play sound pocket_insert

    hide screen sms with Dissolve(1.0)

    "That's enough internet for today."
