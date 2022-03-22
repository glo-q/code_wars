# CodeWars Python Solutions

---

## Summing a number's digits


### Description:

Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.


### Solution


```Python
def sum_digits(number):
    list_of_nums = [int(num) for num in str(abs(number))]
    return sum(list_of_nums)
```

---
### Comment

I had to pass to stupid test in some way ;)


[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
