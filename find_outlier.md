# CodeWars Python Solutions

---

## Find The Parity Outlier


### Description:
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.


### Solution


```python
def find_outlier(integers):
    x = [num for num in integers if num % 2 == 0]
    y = [num for num in integers if num % 2 != 0]
    if len(x) == 1:
        return x[0]
    else:
        return y[0]
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
