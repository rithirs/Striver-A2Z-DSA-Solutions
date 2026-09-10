"""
Problem: Palindrome Number
LeetCode: 9
Striver Sheet: Step 1.4 - Check Palindrome
Time Complexity: O(log10(n))
Space Complexity: O(1)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        original = x
        rev_num = 0
        while x > 0:
            last = x%10
            rev_num = (rev_num * 10) + last
            x //= 10
        return original == rev_num