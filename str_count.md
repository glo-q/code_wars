# CodeWars Python Solutions

---

## All Star Code Challenge #18


### Description:

Create a function that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

### Examples:

```
("Hello", "o")  ==>  1
("Hello", "l")  ==>  2
("", "z")       ==>  0
```


### Solution


```python
def str_count(strng, letter):
    return strng.count(letter)
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
