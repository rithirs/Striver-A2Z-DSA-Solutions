"""
Problem: LC 1 - Two Sum
Approach:
  - Used a hash map (`seen`) mapping values to their indices for O(1) lookups.
  - Iterated through `nums` using `enumerate(nums)`.
  - For each element `num`, calculated its complement: `needed = target - num`.
  - If `needed` already exists in `seen`, returned `[seen[needed], i]`.
  - Otherwise, stored `seen[num] = i` and continued.

Complexity:
  - Time Complexity: O(N) — Single pass traversal; dictionary lookups are O(1) on average.
  - Space Complexity: O(N) — Auxiliary space for the hash map storing at most N elements.

Learnings & Gotchas:
  - Check the map BEFORE inserting the current number so an element cannot pair with itself.
  - Hash map lookup trades O(N) memory to cut brute-force runtime down from O(N^2) to O(N).
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i