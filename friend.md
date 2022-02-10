# CodeWars Python Solutions

---

## Friend or Foe?



### Task
If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...



### Examples
```
friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
```


---


### Solution


```python
def friend(x):
    return [i for i in x if len(i) == 4]
        
```

---
### Comment


[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
