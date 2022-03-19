# CodeWars Python Solutions

---

## The Hashtag Generator


### Description:
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

### Examples:

```
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
```




### Solution


```python
def generate_hashtag(s):
    if len(s) > 140 or len(s) == 0:
        return False
    else:
        s = s.split()
        capitalized = [x.capitalize() for x in s]
        hashtag = "#"
        for char in capitalized:
            hashtag += char
        return hashtag

```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
