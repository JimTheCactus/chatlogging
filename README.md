# Ren'Py Chat Log

***Tools for easily displaying scrolling chat logs in Ren'Py.***

To use this you'll need to do the following steps:

* Copy the `chatlog` folder from `game/scripts` to your `game` folder.
* Create a `ChatLog` object to hold the chat log and state. Use
`default <var> = ChatLog()` to have the log survive saves and rollback.
* Create a wrapper screen and add `use chat_log(<your ChatLog object>)` to it.
* Use `show screen` to show your wrapper screen.
* Call `ChatLog.add_chat()` to add lines of chat to the chat log.


If you've done all of that correctly, your screen should display, the chat log
will automatically include any new items. Additionally, any time you add a new
item, it should automatically scroll the log to the end.

Below is the barest minimum example:
```renpy
# Make a full screen frame
screen logframe(log):
    frame:
        use chat_log(log)

# Initialize the chat log
default mylog = ChatLog()

label start:
    show bg room
    # Show the chat log screen and frame
    show screen logframe(mylog)

    # Add a message to the chat log.
    $ mylog.add_chat(msg="Hello World",
        nick="PoorLifeChocies",
        avatar="chat.png")
```

A more complete example is provided in `game/scripts/example.rpy`.

## Licenses
Copyright 2019 John-Michael O'Brien

### Source Code - MIT License
Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

### Media - Creative Commons Attribution 4.0 International License
Graphics and audio components of this work with the exception of `no.jpg` are
licensed under a Creative Commons Attribution 4.0 International License.
http://creativecommons.org/licenses/by/4.0/
