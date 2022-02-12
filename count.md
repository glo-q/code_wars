# CodeWars Python Solutions

---

## Count characters in your string



### Task
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}

---


### Solution


```python
def count(string):
    list = {}
    for i in string:
        list[i] = string.count(i)
    return list
        
```

---
### Comment


[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
