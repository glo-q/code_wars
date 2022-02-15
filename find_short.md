# CodeWars Python Solutions

---

## Shortest Word



### Description:

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

---


### Solution


```python
def find_short(s):
    return min([len(x) for x in s.split()])
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
