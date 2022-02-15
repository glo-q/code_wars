# CodeWars Python Solutions

---

## Categorize New Member



### Description:

The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with
an application form that will tell prospective members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club,
handicaps range from -2 to +26; the better the player the lower the handicap.

Input will consist of a list of pairs. Each pair contains information for a single potential member.
Information consists of an integer for the person's age and an integer for the person's handicap.

Output will consist of a list of string values (in Haskell: Open or Senior) stating whether the respective
member is to be placed in the senior or open category.


---


### Solution


```python
def open_or_senior(data):
    category = []
    for x in data:
        if (x[0]) >= 55 and (x[1] > 7):
            category += ("Senior",)
        else:
            category += ("Open",)
    return category
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
