# Problem 3: Max subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

# About the solution
For this problem, first I found an O(n2) [solution](solution_optional.py). Next, I could find a pretty simple O(n) [one](solution.py). 

[The first one](solution_optional.py) iterates the array and subarrays looking for the maximum sum. Using this one, it's possible to return the sub-indices, that is, from where the maximum sum starts and ends.  This is kinda straightforward, we just need to compute the local sums and find the maximum. Although it solves the problem, we can make it better.

[The second solution](solution.py), which is the best one, we can't find the sub-indices, only the max sum. But this is the problem goal. To do so, we iterate over the array once computing the local max up to the current value and compute global max considering the past ones.