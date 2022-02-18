# CodeWars Python Solutions

---

## Quarter of the year


### Description:

Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.


---


### Solution


```python
import math

def quarter_of(month):
    return math.ceil(month/3)
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
