# CodeWars Python Solutions

---

## Convert number to reversed array of digits



### Description:

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

### Example

```
348597 => [7,9,5,8,4,3]
0 => [0]
```

---


### Solution


```python
def digitize(n):
    n = list(map(int, str(n)))
    n.reverse()
    return n
        
```

---
### Comment


[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
