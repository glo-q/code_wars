# CodeWars Python Solutions

---

## Is it a palindrome?


### Description:

Write a function that checks if a given string (case insensitive) is a palindrome.


### Solution


```python
def is_palindrome(s):
    return s.lower() == (s[::-1]).lower()
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
