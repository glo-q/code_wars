# CodeWars Python Solutions

---

## Get Count


### Description:

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

### Solution


```python
def get_count(sentence):
    count = [each for each in sentence if each in "aeiou"]
    return len(count)
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
