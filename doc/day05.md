# Regex

Sometimes, as in [2015, day 5](https://adventofcode.com/2015/day/5), we can solely rely on [regular expression](https://en.wikipedia.org/wiki/Regular_expression) to solve the problem.

I've been using regex sometimes to group elements from the input strings, but in this one it represents the core part of the solving algorithm.

To solve the first part, we need to find strings that contains:

* at least three vowels;
* at least one letter that appears twice in a row;
* does **not** contain the strings `ab`, `cd`, `pq`, or `xy`.

This easily translates to:

```python
if len(findall(r"[aeiou]", line)) >= 3 \
        and search(r"([a-z])\1", line) \
        and not search(r"ab|cd|pq|xy", line):
    nice += 1
```

The function [re.findall](https://docs.python.org/3/library/re.html#re.findall) counts the vowels and [re.search](https://docs.python.org/3/library/re.html#re.search) simply finds if the patterns are present (for letters that repets once) or not (for the forbidden pairs).

For the second part, the rules are:

* contains a pair of any two letters that appears at least twice in the string without overlapping;
* contains at least one letter which repeats with exactly one letter between them.

It is a bit more tricky, but not much:

```python
if search(r'([a-z]{2}).*\1', line) \
        and search(r'([a-z]).\1', line):
    nice += 1
```

First condition finds any group with length 2 that repeats itself with with something between them (no overlapping!). Second condition finds any letter that repeats itself with exactly one character between them.

So there it is, the first problem easily solved by regular expression.
