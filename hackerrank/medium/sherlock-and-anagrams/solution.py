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
