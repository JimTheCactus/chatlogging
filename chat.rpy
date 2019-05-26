"""
Tools for displaying scrolling chat logs.

To use this, you will need to create a ChatLog object to hold the chat
logs and associated adjuster context.

Next, you will need to create a screen that uses the chat log screen. The chat
log screen will automatically expand to fill the entire space it is placed in,
so an explicitly sized frame is a good choice.

Once these steps are done, display your screen and use add_chat to add lines
to the chat. The chat log will automatically scroll to the new item.
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


define chat_infinity_float = float("inf")
init python:
    class ChatLog:
        """
        Thanks to milkymalk at
        https://lemmasoft.renai.us/forums/viewtopic.php?t=44711
        for the idea here. I refined the implementation a bunch, but it's their
        core suggestion that helped.
        """
        def __init__(self):
            # Create a blank list for the chats.
            self._chats = []
            # And make the adjustment for our screen.
            self._adj = ui.adjustment()
        def add_chat(self, type="chat_entry", **kwargs):
            """
            Adds a new chat entry.

            type - selects the name of the screen that will display this line
                of chat.

            Additional named arguments will need to be provided based on the
            arguments the screen that displays the line. For the default
            chat_entry screen, this will be msg, nick, and avatar.

            For example:
                mychat.add_chat(type="chat_entry", msg="Hello world",
                    nick="darkflamemaster", avatar="dfm chat avatar")
            """
            self._chats.append((type, kwargs))
            return len(self._chats)-1
        def history(self):
            """ Returns the list of chat lines. """
            return self._chats
        def adjustment(self):
            """ Returns the adjustment. Needed by the chat log screen """
            return self._adj;
