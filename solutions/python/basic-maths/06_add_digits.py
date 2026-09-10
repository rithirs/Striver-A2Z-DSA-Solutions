"""
Problem: Add Digits (Digital Root)
LeetCode: 258
Time Complexity: O(log10(n))
Space Complexity: O(1)
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sum = 0
            while num > 0:
                last = num % 10
                sum += last
                num //= 10
            num = sum
        return num