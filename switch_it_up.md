# CodeWars Python Solutions

---

## Switch it Up!



### Description:

When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

---


### Solution


```python
def switch_it_up(number):
    switch = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        0: "Zero"
    }
    return switch.get(number)
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
