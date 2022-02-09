# CodeWars Python Solutions

---

## The highest profit wins!



### Task
Write function bmi that calculates body mass index (bmi = weight / height2).


### Examples
```
if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
```


---


### Solution


```python
def bmi(weight, height):
    score = weight / (height * height)
    if score <= 18.5:
        return "Underweight"
    elif score <= 25:
        return "Normal"
    elif score <= 30:
        return "Overweight"
    else:
        return "Obese"
        
```

---
### Comment


[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
