# CodeWars Python Solutions

---

## Find smallest integer


### Description:

Given an array of integers your solution should find the smallest integer.

### Examples:

```
Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
```

### Solution


```python
def find_smallest_int(arr):
    lst = sorted(arr, key=int)
    return lst[0]
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
