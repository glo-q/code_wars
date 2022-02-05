# ATMs allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6
# digits.
#
# If the function is passed a valid PIN string, return true, else return false.
#
# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

import re


def validate_pin(pin):
    if re.findall("\d\d\d\d", pin) and len(pin) == 4:
        return True
    elif re.findall("\d\d\d\d\d\d", pin) and len(pin) == 6:
        return True
    else:
        return False

# Best I found:
# def validate_pin(pin):
#     return len(pin) in (4, 6) and pin.isdigit()
