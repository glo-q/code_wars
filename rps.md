# CodeWars Python Solutions

---

## Rock Paper Scissors!

### Task
Let's play! You have to return which player won! In case of a draw return Draw!.

```
rps('scissors','paper') // Player 1 won!
rps('scissors','rock') // Player 2 won!
rps('paper','paper') // Draw!
```


---


### Solution


```python
def rps(p1, p2):
    sc = "scissors"
    pp = "paper"
    rc = "rock"
    if p1 == p2:
        return "Draw!"
    elif p1 == sc and p2 == pp:
        return "Player 1 won!"
    elif p1 == pp and p2 == rc:
        return "Player 1 won!"
    elif p1 == rc and p2 == sc:
        return "Player 1 won!"
    else:
        return "Player 2 won!"
```

---
### Comment

Oh, I know, simple as that.

That one I found most interesting:

```python
def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]
```

[See on CodeWars.com](https://www.codewars.com/users/ITRonin)
