# CodeWars Python Solutions

---

## Shortest Word



### Description:

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

---


### Solution


```python
def create_phone_number(n):
    for x in range(len(n)):
        return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
        
```

---
### Comment

Well...
```python
def find_short(s):
    return min([len(x) for x in s.split()])
```



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
