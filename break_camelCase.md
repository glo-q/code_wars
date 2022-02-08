# CodeWars Python Solutions

---

## Break camelCase

### Task
Complete the solution so that the function will break up camel casing, using a space between words.

```
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
```


---


### Solution


```python
import re


def solution(s):
    return " ".join(map(str, re.split(r"(?=[A-Z])", s)))
```

---


[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
