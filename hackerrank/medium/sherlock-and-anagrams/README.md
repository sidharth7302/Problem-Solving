# Sherlock and Anagrams

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Two strings are [*anagrams*][123] of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.  

**Example**  
$s = mom$  

The list of all anagrammatic pairs is $[m, m], [mo, om]$ at positions $[[0], [2]], [[0, 1], [1, 2]]$ respectively.

[123]: http://en.wikipedia.org/wiki/Anagram  

**Function Description**

Complete the function *sherlockAndAnagrams* in the editor below.  

sherlockAndAnagrams has the following parameter(s):

-  *string s:* a string  

**Returns**  

- *int:* the number of unordered anagrammatic pairs of substrings in $s$

**Input Format**

The first line contains an integer $q$, the number of queries.   
Each of the next $q$ lines contains a string $s$ to analyze. 

**Constraints**

$1 \le q \le 10$   
$2 \le \text{ length of }s \le 100$  
$s$ contains only lowercase letters in the range ascii[a-z]. 

**Output Format**

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-13T09:43:25.037Z  

```py
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    substring_counts = Counter()
    n = len(s)
    for length in range(1, n):
        for i in range(n - length + 1):
            sub = s[i:i+length]
            sorted_sub = "".join(sorted(sub))
            substring_counts[sorted_sub] += 1
    total_pairs = 0
    for count in substring_counts.values():
        if count > 1:
            total_pairs += (count * (count - 1)) // 2
            
    return total_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

```

---

[View on HackerRank](https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem)