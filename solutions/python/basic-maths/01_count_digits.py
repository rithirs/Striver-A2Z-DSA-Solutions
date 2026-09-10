"""
Problem: Count Digits That Divide a Number
LeetCode: 2520
Striver Sheet: Step 1.4 - Count Digits
Time Complexity: O(log10(n))
Space Complexity: O(1)
"""

class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        count = 0
        while num > 0:
            last = num%10
            if temp % last == 0: count+=1
            num//=10
        return count