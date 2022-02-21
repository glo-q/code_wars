# CodeWars Python Solutions

---

## Human Readable Time


### Description:

Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

### Solution


```python
def make_readable(seconds):
    hours = seconds // 3600
    minutes = ((seconds % 3600) // 60)
    seconds = ((seconds % 3600) % 60)

    def zeros(m):
        if m < 10:
            return "0" + str(m)
        else:
            return m

    return f"{zeros(hours)}:{zeros(minutes)}:{zeros(seconds)}"
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
