# CodeWars Python Solutions

---

## Reversed Words


### Description:

Complete the solution so that it reverses all of the words within the string passed in.

### Examples:

```
"The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

```


### Solution


```python
def reverse_words(s):
    return " ".join(s.split()[::-1])

```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
