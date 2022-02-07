'''
Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo"
name + " does not play banjo"
Names given are always valid strings.
'''


import re


def are_you_playing_banjo(name):
    if re.findall("\Ar", name.lower()):
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

# I just wanted to use RegEx ;)
