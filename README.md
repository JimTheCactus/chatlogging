# Ren'Py Chat Log

***Tools for easily displaying scrolling chat logs in Ren'Py.***

To use this you'll need to do the following steps:

* Copy `chat.rpy` and `chat_screens.rpy` to your `game` folder.
  * Optionally, you can import this library as a Git submodule in your `game` folder to make updating easy. See [git-submodule](https://git-scm.com/docs/git-submodule) and the [Git Book discussion on submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) for more information.
* Create a `ChatLog` object to hold the chat log and state. Use
`default <var> = ChatLog()` to have the log survive saves and rollback.
* Create a wrapper screen and add `use chat_log(<your ChatLog object>)` to it.
* Use `show screen` to show your wrapper screen.
* Call `ChatLog.add_chat()` to add lines of chat to the chat log.


If you've done all of that correctly, your screen should display, the chat log
will automatically include any new items. Additionally, any time you add a new
item, it should automatically scroll the log to the end.

## Chat Entries
You'll want to look though `chat_screens.rpy` to see how to make your own
screens and to see what parameters are available for the default provided
screens. That said, the options for the default screens are shown below

### chat_entry
* msg
  * The message to be displayed.
* nick
  * The nickname to be shown with the message. Leave blank for none.
* avatar
  * A name for a displayable image that will be used as the chat user's
  icon. This will be something like "alex chat happy", just like
  you'd use in a show statement.

### chat_picture
* pic
  * AA name for a displayable image that will be included as an image.
  This will be something like "alex chat happy", just like you'd use in a
  show statement.
* nick
  * The nickname to be shown with the message. Leave blank for none.
* avatar
  * A name for a displayable image that will be used as the chat user's
  icon. This will be something like "alex chat happy", just like
  you'd use in a show statement.

## Example
A complete example is provided at [https://github.com/JimTheCactus/chatlogging-example](https://github.com/JimTheCactus/chatlogging-example).
However, a bare minimum example is below. It will make a full screen chat log and add
a single chat item to it using the default `chat_entry` entry type which takes
`msg`, `nick`, and `avatar` inputs.

```renpy
# Make a full screen frame
screen logframe(log):
    frame:
        use chat_log(log)

# Initialize the chat log
default mylog = ChatLog()

label start:
    scene
    # Show the chat log screen and frame
    show screen logframe(mylog)

    # Add a message to the chat log.
    $ mylog.add_chat(msg="Hello World",
        nick="PoorLifeChocies",
        avatar="chat.png")
```

## Licenses
Copyright 2019 PoorLifeChoices <John-Michael O'Brien>

No reason to make this needlessly hard. To use this in your own work, do the following:

* Put something to the effect of `Chat log script by PoorLifeChoices` (lol :3) or `Chat log script by John-Michael O'Brien` in your credits.
* Use the thing.
* Love the thing.
* Make a million dollars from your thing with my thing.
* It ain't my fault if the thing breaks something important.

However, I formally have to be more specific, so legalese ho!

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
