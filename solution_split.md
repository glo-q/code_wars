# CodeWars Python Solutions

---

## Split Strings


### Description:

Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').


### Examples:

```
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
```

### Solution


```python
import re

def solution(s):
    if len(s) % 2 != 0:
        s += "_"
    return re.findall("..", s)
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
