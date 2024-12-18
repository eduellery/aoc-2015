# Itertools

To solve [2015, day 9](https://adventofcode.com/2015/day/9) we start using the [itertools](https://docs.python.org/3/library/itertools.html) library.

As it says in its description, it is a collection of:

> Functions creating iterators for efficient looping

Some examples of useful functions are combinatoric iterators such as:

* [combinations](https://docs.python.org/3/library/itertools.html#itertools.combinations) to generate something as\
  `combinations('ABCD', 2) --> AB AC AD BC BD CD` or `combinations(range(4), 3) --> 012 013 023 123` 
* [permutations](https://docs.python.org/3/library/itertools.html#itertools.permutations) to generate something as\
  `permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC` or `permutations(range(3)) --> 012 021 102 120 201 210`

Doing this by hand is not hard, but just unnecessary with the existence of this library.

Other good examples are:

* Infinite iterators:
  * [count](https://docs.python.org/3/library/itertools.html#itertools.count) to do slice-like operations, as explained in [day 3](day03.md) like `count(2.5, 0.5) -> 2.5 3.0 3.5 ...`
  * [cycle](https://docs.python.org/3/library/itertools.html#itertools.cycle) to keep looping as `cycle('ABCD') --> A B C D A B C D A B C D ...`
* Iterators terminating on the shortest input sequence:
  * [accumulate](https://docs.python.org/3/library/itertools.html#itertools.accumulate) to do progressions as\
  `accumulate([1,2,3,4,5]) --> 1 3 6 10 15` or `accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120`
  * [groupby](https://docs.python.org/3/library/itertools.html#itertools.groupby) to do DB-like grouping as `[list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D`

With this library the solutions are more elegant, concise and very handy for those speed-running the solution.
