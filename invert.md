# CodeWars Python Solutions

---

## Invert values


### Description:

Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

```
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
```


---


### Solution


```python
def invert(lst):
    return [-x for x in lst]
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
