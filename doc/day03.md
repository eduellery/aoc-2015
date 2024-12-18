# Slice

To solve [2015, day 3](https://adventofcode.com/2015/day/3), the first part is straightforward in every language: just iterate over the elements and keep track of the houses visited by Santa.

```python
for direction in directions:
    santa = self.move(santa, direction)
    houses.add(santa)
```

For the second part, even though it is still simple, some languages require to keep track of the current index in the loop to mark the houses visited by Santa and houses visited by Robot-Santa.

If you aare using Python though, it becomes much easier using [slice](https://docs.python.org/3/library/functions.html#slice). There is a great explanation [here](https://stackoverflow.com/questions/509211/understanding-slice-notation).

So instead of some boilerplate code to control the iterations, you just have to move Santa every 2 elements and Robot-Santa every 2 elements, starting at 0 and 1 respectively.
 
```python
santa_houses = self.visited_houses(self.directions[0::2])
robot_houses = self.visited_houses(self.directions[1::2])
```

Slice makes life much easier!
