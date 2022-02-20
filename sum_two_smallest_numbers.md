# CodeWars Python Solutions

---

## Sum of two lowest positive integers


### Description:

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.

### Solution


```python
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
