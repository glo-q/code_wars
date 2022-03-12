# CodeWars Python Solutions

---

## Parse nice int from char problem


### Description:

Ask a small girl - "How old are you?". She always says strange things... Lets help her!

For correct answer program should return int from 0 to 9.

Assume test input string always valid and may look like "1 year old" or "5 years old", etc.. The first char is number only.


### Solution


```python
import re

def get_age(age):
    x = "".join(map(str, re.findall("[0-9]", age)))
    return int(x)
```

---
### Comment

Haha ;) I really overcomplicated this task, but I like regex. return int(age[0]) would be enough.



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
