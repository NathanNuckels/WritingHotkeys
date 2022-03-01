# WritingHotkeys

Usage:

```python main.py [<COMMAND> [ARGS...]```

Runs a custom command. There are no commands currently. I am trying to come up with some ideas.

```python new.py <FILENAME> <TITLE> <AUTHOR> [-d date] [PACKAGES...]```

!! This commmand is up for review. !!

Creates a new LaTeX file with the given title author, date, and packages. It also includes `fancyhdr` by default.

```python findreplace.py <INPUT-FILE> <TEMPLATE> [OUTPUT-FILE]```

Runs find and replace according to a template file. I use it to convert my code words
into their regular meaning. Also useful for abriviations.

Example of a template file:
```
alt > altitude
ld > lucid dream
irl > in real life
```

Note that you *can* copy a `>` verbaitum, but not `_>_`.
Eg. `3>1 > 300>100` is ok, `3>1 > 300 > 100` is also *technically* ok but `3 > 1 > 300 > 100` is not.

```python autoreplace.py [TEMPLATE]```

Instead if finding and replacing stuff in a file, it will directly
log what you type on your keyboard and replace it. For example, you
can type `@@` into ANY textbox and it will be replaced with 
`my.super.long.email@the.email.com`
or whatever. This is my favorate one.

```python levelup.py [bool: DELETE] [int: NUMBER OF MESSAGES] [float: DELAY]```

A basic script to level up in Discord. If delete is true, it will delete the message after it sends it.
You can also set the number of messages to send. The delay varible sets the delay in secconds between messages.
if delete is false, it should be greater than 1. If delete is true it should be greater than 2. 
