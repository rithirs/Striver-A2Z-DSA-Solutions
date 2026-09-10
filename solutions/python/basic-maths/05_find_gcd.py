"""
Problem: Find Greatest Common Divisor
LeetCode: 1979
Striver Sheet: Step 1.4 - Find GCD / HCF (Euclidean Algorithm)
Time Complexity: O(log(min(a, b)))
Space Complexity: O(1)
"""
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)
        
        while b != 0:
            a, b = b, a % b
            
        return a