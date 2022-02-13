# CodeWars Python Solutions

---

## Reverse words



### Task
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

### Examples:

```
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
```

---


### Solution


```python
def reverse_words(text):
    return " ".join(word[::-1] for word in text.split(" "))
        
```

---
### Comment


[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
