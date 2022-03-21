# CodeWars Python Solutions

---

## Credit Card Mask


### Description:

Your task is to write a function maskify, which changes all but the last four characters into '#'.

### Examples:

```
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"
```


### Solution


```Python
def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        mask = len(cc)-4
        return mask*"#" +cc[-4:]
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
