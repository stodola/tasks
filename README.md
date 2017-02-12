# tasks

Task 1.
Solution: battle.py

I think I found two  mistakes in this task. In section with headline 'Examples with negative integers:' in example two result should be 'odds win'. In example 3 binary representation of 17 is wrong, result should be 'evens win'.

Task 2.
Solution: minimum_effort.py

This task was harder than the first one.

Firstly I thought I will have to use backtracking, but I very fast realized it is unnecessary, because I have to check all solutions anyways.

So I wrote an algorithm that uses simple recursion, file: additions/recursive_solution.py.

The computation complexity of this algorithm is O(2^N). Check picture plot1.png in additions to see run times of bigger tables, code: additions/timing_recursive.py.

If I wouldn't have Internet access that would by my solution, I planned to add small optimization by keeping track of most efficient way computed so far and breaking from recursion when another solution exceeds this number, but ...

For the first glance at this exercise it looked for my very pl.spoj.com likish, so I started digging and found a hint, that it can be done by using dynamic programming. Knowing that I implemented solution shown in file minimum_effort.py.

Computational complexity of this algorithm is O(N^2), so it is 'a little bit faster' from recursive algorithm, which I implemented at the beginning. Plot2.png shows run times of bigger tables, code: additions/timing_dynamic.py.
