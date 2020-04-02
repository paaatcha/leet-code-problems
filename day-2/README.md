# Problem 2: Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example 1:
```
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
```

# About the solution
To have fun solving this problem, I decided to try a recursion approach. It can be solved without using recursion, but I'd like to use that. 

To do so, first, we need to decide a stop rule. Doing a quick assess about happy numbers, we see that below 10, only 7 and 1 are happy numbers. So, this is out stop rule.

To compute the sum of powers, let's goind to use python in our favor. First, transform the number to string and then selecting the characters and transforming to int. In the following, we compute the sum:
```
sum([int(c_num)**2 for c_num in str(n)])
``` 

Now, we just need to apply the recursion. 

I'll try to solve it without using recursion as well. But later.