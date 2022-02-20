# CodeWars Python Solutions

---

## Moving Zeros To The End


### Description:

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

### Examples

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

### Solution


```python
def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(i)
    return array
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
