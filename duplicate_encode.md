# CodeWars Python Solutions

---

## Duplicate Encoder


### Description:
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.


### Solution


```python
def duplicate_encode(word):
    word = word.lower()
    encode = ""
    for n in word:
        if word.count(n) == 1:
            encode += "("
        else:
            encode += ")"
    return encode
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
