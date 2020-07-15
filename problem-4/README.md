# Problem 4: Move zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Note:**
You must do this in-place without making a copy of the array.
Minimize the total number of operations.


# About the solution
For this problem, I also proposed two solutions: an [O(n2)](solution_optional.py) and an [O(n)](solution.py). 

[The first solution](solution_optional.py) is a [bubble sort](https://en.wikipedia.org/wiki/Bubble_sort) adaptation. It just swaps adjacent elements if one of them is a zero. However, it doesn't work if we have a sequence of zeros (like `[1,0,0,0,3,2]`). So, I counted the zeros a do the operation for this number. Obviously, it's not the best solution, although it can pass in all test cases.

[The best solution](solution.py) I could find is moving nonzeros rather than zeros. First, we iterate over the array moving the non-zeros to the left. We also count the number of elements we moved. Therefore, we know that from the index array's size minus the number of moving elements to the array's size, we need to fill with zeros.  