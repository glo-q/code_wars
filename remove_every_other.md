# CodeWars Python Solutions

---

## Removing Elements


### Description:

Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

### Example:

```
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
```

None of the arrays will be empty, so you don't have to worry about that!

---


### Solution


```python
def remove_every_other(my_list):
    return my_list[::2]
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
