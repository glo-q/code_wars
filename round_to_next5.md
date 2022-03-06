# CodeWars Python Solutions

---

## Round up to the next multiple of 5


### Description:

Given an integer as input, can you round it to the next (meaning, "higher") multiple of 5?


### Examples:

```
input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.
```

### Solution


```python
import math
def round_to_next5(n):
    return math.ceil(n/5.0) * 5
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
