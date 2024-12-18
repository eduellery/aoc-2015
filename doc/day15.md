# Custom Taylored Functions

On [2015, day 15](https://adventofcode.com/2015/day/15) it was the first time we had to create separate functions for the test input and the actual input.

So far we tried to rely on the same code to process all the inputs. The following approach makes no sense in real life development.
We can't test something on a piece of code that only serves the test itself and leave the "production code" to run untested.

So why do I did like that? This answer can touch some interesting topics:

1. Rules are not the absolute truth, they are guidelines that should be followed all the time *unless* we have a *really strong* reason to break it, considering all the factors covered by the rule in question.
2. There is no production code here. *Everything* in AOC is a test, the only difference is:
   1. Part of it is a small set, easier to debug and to compute and for which we know the answer
   2. Part of it is our user input, harder to debug and to compute and for which the website will tell us if we got the right value (and we update our test accordingly)
3. The simpler solution consists of several loops depending on the input ingredients. So the smaller set solution is just a regular `for` while the larger set is processed by 3 nested `for`.

Could I make a generic solution that would process any number of igredients present in the input? Yeah. But it could be harder to understand, take more time to implement, we won't process more than these 2 cases etc.

So taking everything into consideration, I decided to split the code for different inputs. 🤷🏽‍♂️
