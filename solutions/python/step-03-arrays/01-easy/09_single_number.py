"""
Problem: LC 136 - Single Number
Approach:
  - Initialized an accumulator variable `ans = 0`.
  - Iterated through every number in `nums` and accumulated using the bitwise XOR operator (`ans ^= num`).
  - Exploited the properties of XOR:
      1. a ^ 0 = a
      2. a ^ a = 0 (identical pairs cancel out to 0)
      3. Commutative & associative (order of elements does not matter)
  - Every pair cancels itself out to 0, leaving only the unique single number.

Complexity:
  - Time Complexity: O(N) — Single pass through the array.
  - Space Complexity: O(1) — Uses only a single integer variable.

Learnings & Gotchas:
  - Avoided checking adjacent elements because the array is not sorted.
  - Hash maps or sets solve this easily but cost O(N) auxiliary space; bitwise XOR achieves true O(1) space.
"""
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count = 0
        for i in nums:
           count^=i
        return count