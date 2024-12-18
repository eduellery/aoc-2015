# Lambda

To solve [2015, day 11](https://adventofcode.com/2015/day/11) we use [lambda](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions) for the first time. They are small anonymous functions that should adhere to some rules:

> Lambda functions can be used wherever function objects are required.
> They are syntactically restricted to a single expression.
> Semantically, they are just syntactic sugar for a normal function definition.

When using the `sub` method, this is the documentation

> Return the string obtained by replacing the leftmost
> non-overlapping occurrences of the pattern in string by the
> replacement repl.  repl can be either a string or a callable;
> if a string, backslash escapes in it are processed.  If it is
> a callable, it's passed the Match object and must return
> a replacement string to be used.

So to set our `repl` parameter we could use a regular function, but why not simply expliciting the transformation inline? This is when `lambda` comes in hand:

```python
sub(r'([a-y])(z*)$', lambda x: chr(ord(x.group(1)) + 1) + len(x.group(2)) * "a", password)
```

We are going to use it again in other solutions to make them look cleaner.
