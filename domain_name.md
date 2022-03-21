# CodeWars Python Solutions

---

## Extract the domain name from a URL


### Description:

Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. 

### Examples:

```
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
```


### Solution


```Python
def domain_name(url):
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("www.", "")
    url = url.split(".")
    return url[0]
```

---
### Comment



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
