# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case
# insensitive. The string can contain any char.
#
# Examples input/output:
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    if s == "":
        return True
    for i in s:
        if (s.count("o") + s.count("O")) == (s.count("x") + s.count("X")):
            return True
        return False


# OMG, it was so obvious:
# def xo(s):
#     s = s.lower()
#     return s.count('x') == s.count('o')
