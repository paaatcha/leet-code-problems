# Problem 1: Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

**Note:** Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
```
Input: [2,2,1]
Output: 1
```
Example 2:
```
Input: [4,1,2,1,2]
Output: 4
```

# About the solution
The easiest way to solve this problem is by using a hash table. First, we select the elements that repeat in the list. Next, we choose that one which doesn't repeat. However, there is an important note. We need to present an algorithm in linear time. So, the trick of this problem is to use the XOR operator!

## What is the XOR operator?
First of all, XOR (e**x**clusive **or**) is a binary operation that takes two bits and results in 1 if **only one** bit is one. Example:


a | b | a ^ b
--|---|------
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0

This operation may be performed using two integers. In this case, the XOR is performed between each corresponded bit. For example: 

```
12 ^ 8 = 4
1100 ^ 1000 = 0100
```

This operation is commutative and associative, that is, let us consider three binary numbers `b1, b2, b3`. 
- **Commutative means:** `b1 ^ b2 ^ b3` is equal to any combination `b1 ^ b3 ^ b2`, `b2 ^ b1 ^ b3`, and so on.
- **Associative means:** we can associate the numbers in any form:  `b1 ^ b3 ^ b2` is equal to `b1 ^ (b3 ^ b2)` that is equal to `(b1 ^ b3) ^ b2` and so on.


 Obviouslly, any number XOR zero is equal to the number (Ex: `12 ^ 0 = 12`) and any number XOR itself is 0 (Ex: `12 ^ 12 = 0`).

 It's possible to mask a number using the XOR, for example:
 ```
 12 ^ 8 = 4
 4 ^ 8 = 12
 ```

 In this case, the mask is 4.

 ## Solving the problems
 Now we know a little bit more about XOR, it's easy to understand the solution. Let us consider a list `L = [1, 2, 3, 3, 2`].

 Performing the loop: 
 ```
 x = 0
for l in L:
    x ^= l
```

We are doing: `x = 1 ^ 2 ^ 3 ^ 3 ^ 2`. Considering the properties explained above, we can do:
```
x = 1 ^ (2 ^ 2) ^ (3 ^ 3)
x = 1 ^ (0) ^ (0)
x = 1
```

Thus, we selected the single number that doesn't repeat in the array. 