# CodeWars Python Solutions

---

## Testing 1-2-3



### Task
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

### Examples:

```
number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]
```


---


### Solution


```python
def number(lines):
    return [f"{i + 1}: {lines[i]}" for i in range(len(lines))]
        
```

---
### Comment


[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
