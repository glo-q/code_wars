# CodeWars Python Solutions

---

## Stop gninnipS My sdroW!


### Description:
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"



### Solution


```python
def spin_words(sentence):
    sentence = sentence.split()
    new_sent = []
    for word in sentence:
        if len(word) > 5:
            new_sent.append(word[::-1])
        else:
            new_sent.append(word)

    return " ".join(new_sent)
```

---
### Comment

Yes I know. I can make it one-liner. But I'm completely tired and want to write a readable code.



[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
