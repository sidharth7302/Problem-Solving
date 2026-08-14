# Contains Duplicate

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer array `nums`, return `true` if any value appears  **at least twice**  in the array, and return `false` if every element is distinct.

 

 **Example 1:** 

 **Input:**  nums = [1,2,3,1]

 **Output:**  true

 **Explanation:** 

The element 1 occurs at the indices 0 and 3.

 **Example 2:** 

 **Input:**  nums = [1,2,3,4]

 **Output:**  false

 **Explanation:** 

All elements are distinct.

 **Example 3:** 

 **Input:**  nums = [1,1,1,3,3,4,3,2,4,2]

 **Output:**  true

 

 **Constraints:** 

- 1 <= nums.length <= 105
- -109 <= nums[i] <= 109

## Solution

**Language:** Python  
**Runtime:** 52 ms (beats 8.80%)  
**Memory:** 39.3 MB (beats 6.67%)  
**Submitted:** 2026-08-14T16:19:59.943Z  

```py
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prevmap={}
        flag=0
        for i,nu in enumerate(nums):
            if nu in prevmap:
                flag+=1
            else:
                prevmap[nu]=i
        if flag==0:
            return False
        else:
            return True   



```

---

[View on LeetCode](https://leetcode.com/problems/contains-duplicate/)