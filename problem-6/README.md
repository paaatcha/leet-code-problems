# Problem 6: Group Anagrams
Given an array of strings, group anagrams together.

Given an array of strings, group anagrams together.

Example:
```
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

**Note:**
- All inputs will be in lowercase.
- The order of your output does not matter.


# About the solution
This problem is super simple to solve using Python. We just need to track the anagram letters using a `dict` and then organize them.