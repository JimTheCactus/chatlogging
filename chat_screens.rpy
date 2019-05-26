"""
Tools for displaying scrolling chat logs.

These define the various screens necessary for the chat log. chat_entry and
chat_picture are provided as examples, but more creative layouts are possible.
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


# Defines a log box that, when handed a ChatLog object, will maintain an
# autoscrolling chat.
screen chat_log(log):
    viewport id "chatlog":
        yadjustment log.adjustment()
        mousewheel True
        draggable True
        yinitial 1.0
        python:
            # Thanks to mangoduck at
            # https://lemmasoft.renai.us/forums/viewtopic.php?t=32584 for this
            # flash of insight for auto scrolling
            log.adjustment().value = chat_infinity_float
        vbox:
            spacing 10

            for type, kwargs in log.history():
                use expression type pass (**kwargs)

# Defines a single line of the chat log.
# The format is Discord-like.
# avatar nick
#   "    msg
screen chat_entry(msg="", nick=None, avatar=None):
    hbox:
        spacing 10
        if avatar != None:
            add avatar
        vbox:
            if nick != None:
                text nick
            text msg

# Defines a line with a picture on it
# The format is Discord-like.
# avatar nick
#   "    pic
screen chat_picture(pic=None, nick=None, avatar=None):
    hbox:
        spacing 10
        if avatar != None:
            add avatar
        vbox:
            if nick != None:
                text nick
            if nick != None and pic != None:
                null height 10
            if pic != None:
                add pic
