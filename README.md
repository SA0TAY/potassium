# potassium
Highlight call signs in WSJT-X which are currently spotted doing POTA.

This is currently a messy proof of concept, but it will eventually be expanded
into something more robust.

## Prerequisites
This guide assumes that you are using WSJT-X with multicast configured and
enabled. There are plenty of guides floating about on how to set this up, so I
will leave this bit as an exercise for the reader.

This guide also assumes basic familiarity with the terminal. If you're expecting
a cushy user interface, I'm afraid you will have to wait until I've had the time
and gumption to flesh this thing out a bit. Pull requests are welcome as always.

## Usage
First, copy `docs/settings.ini.example` to `settings.ini` and modify it as
needed. Then, run `potassium/__init__.py` from the project's root directory.
When a spotted call sign shows up as the caller on WSJT-X, this program will a)
output the call sign on the console, b) highlight the call sign in WSJT-X using
a nice, eye-catching blue/yellow combination.

The list of spotted POTA activators is updated every 60 seconds, which seems to
be on par with the expected API load. Please don't decrease this cooldown time.
