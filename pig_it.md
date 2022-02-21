# CodeWars Python Solutions

---

## Simple Pig Latin


### Description:

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

### Examples:

```
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
```

### Solution


```python
def pig_it(text):
    pig_list = []
    for i in text.split():
        if i.isalnum():
            pig_list.append(i[1:] + i[:1] + "ay")
        else:
            pig_list.append(i)
    return " ".join(pig_list)
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
