# CodeWars Python Solutions

---

## If you can't sleep, just count sheep!!


### Description:

Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.


### Solution


```python
def count_sheep(n):
    string = ""
    for i in range(n):
        string += f"{i+1} sheep..."
    return string

```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
