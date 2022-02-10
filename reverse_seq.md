# CodeWars Python Solutions

---

## Reversed sequence



### Task
Build a function that returns an array of integers from n to 1 where n>0.


### Examples
```
n=5 --> [5,4,3,2,1]
```


---


### Solution


```python
def reverse_seq(n):
    return [*range(n, 0, -1)]
        
```

---
### Comment


[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
