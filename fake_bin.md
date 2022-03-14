# CodeWars Python Solutions

---

## Fake Binary


### Description:
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string




### Solution


```python
def fake_bin(x):
    new_fake_bin = ""
    for i in x:
        if int(i) < 5:
            new_fake_bin += "0"
        else:
            new_fake_bin += "1"
    return new_fake_bin
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
