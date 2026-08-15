# Maximum Product Subarray

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array `nums`, find a subarray that has the largest product, and return  *the product*.

The test cases are generated so that the answer will fit in a  **32-bit**  integer.

 **Note**  that the product of an array with a single element is the value of that element.

 

 **Example 1:** 

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

```

 **Example 2:** 

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

```

 

 **Constraints:** 

- 1 <= nums.length <= 2 * 104
- -10 <= nums[i] <= 10
- The product of any subarray of nums is guaranteed to fit in a 32-bit integer.

## Solution

**Language:** Python  
**Runtime:** 7 ms (beats 37.07%)  
**Memory:** 19.8 MB (beats 43.94%)  
**Submitted:** 2026-08-15T04:50:58.651Z  

```py
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curmax,curmin=1,1
        for n in nums:
            if n==0:
                curmin,curmax=1,1
                continue
            temp=curmax*n
            curmax=max(n*curmax,n*curmin,n)
            curmin=min(temp,n*curmin,n)    
            res=max(res,curmax)
        return res    
```

---

[View on LeetCode](https://leetcode.com/problems/maximum-product-subarray/)