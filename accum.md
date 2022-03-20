# CodeWars Python Solutions

---

## Mumbling


### Description:
This time no story, no theory. The examples below show you how to write function accum:

### Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"




### Solution


```python
def accum(s):
    new_s = ""
    for i in range(len(s)):
        z = s[i]*(i+1)
        new_s += z.capitalize()
        new_s += "-"

    return new_s[0:-1]

```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
