# CodeWars Python Solutions

---

## Abbreviate a Two Word Name

### Task
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

```
Sam Harris => S.H

patrick feeney => P.F
```


---


### Solution


```python
def abbrev_name(name):
    a = name.split(" ")
    return (a[0][0]).upper() + "." + (a[1][0]).upper()
```

---
### Comment


[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
