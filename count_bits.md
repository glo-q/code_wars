# CodeWars Python Solutions

---

## Bit Counting


### Description:

Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

### Example:

```
The binary representation of 1234 is 10011010010, so the function should return 5 in this case
```

### Solution


```python
def count_bits(n):
    binary = "{0:b}".format(n)
    return binary.count("1")
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
