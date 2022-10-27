# CodeWars Python Solutions

---

## Name Shuffler

### Task
Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

```
"john McClane" --> "McClane john"
```


---


### Solution


```python
def name_shuffler(str):
    return " ".join(str.split()[::-1])
```

---
### Comment


[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
