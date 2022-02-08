# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the
# alphabet. ROT13 is an example of the Caesar cipher.
#
# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
# characters included in the string, they should be returned as they are. Only letters from the latin/english
# alphabet should be shifted, like in the original Rot13 "implementation".
#
# Please note that using encode is considered cheating.

def rot13(message):
    list = []
    for i in message:
        i = ord(i)
        if i in range(65, 91):
            if i > 77:
                i -= 13
                list.append(chr(i))
            else:
                i += 13
                list.append(chr(i))
        elif i in range(97, 123):
            if i > 109:
                i -= 13
                list.append(chr(i))
            else:
                i += 13
                list.append(chr(i))
        else:
            list.append(chr(i))
    return "".join(list)
