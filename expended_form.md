# CodeWars Python Solutions

---

## Write Number in Expanded Form


### Description:

You will be given a number and you will need to return it as a string in Expanded Form.

### Example:

```
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
```

NOTE: All numbers will be whole numbers greater than 0.


### Solution


```Python
def expanded_form(num):
    res = []
    for i, n in enumerate(str(num)):
        if n != "0":
            res.append(n + "0" * (len(str(num)[i:])-1))
    return " + ".join(res)
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
