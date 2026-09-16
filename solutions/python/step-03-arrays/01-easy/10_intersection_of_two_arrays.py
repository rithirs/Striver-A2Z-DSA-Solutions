"""
Problem: LC 349 - Intersection of Two Arrays

Approach 1 (Hash Sets - Pythonic):
  - Converted both lists to sets to remove internal duplicates and allow O(1) membership checks.
  - Used the set intersection operator `&` to find shared unique elements.
  - Converted the result back to a list: `list(set(nums1) & set(nums2))`.

Approach 2 (Two Pointers - In-Place/Sorted):
  - Sorted both `nums1` and `nums2` in ascending order.
  - Traversed both arrays simultaneously with pointers `i` and `j`:
      * If nums1[i] < nums2[j]: increment i (nums1[i] is too small to match anything ahead).
      * If nums1[i] > nums2[j]: increment j (nums2[j] is too small to match anything ahead).
      * If nums1[i] == nums2[j]: match found! Appended to result only if it wasn't a duplicate
        of the previously added element (`not result or result[-1] != nums1[i]`), then incremented both pointers.

Complexity:
  - Approach 1 (Hash Sets):
      * Time: O(N + M) — Linear time to create sets and compute the intersection.
      * Space: O(N + M) — Auxiliary space for the hash sets.
  - Approach 2 (Two Pointers):
      * Time: O(N log N + M log M) — Dominated by sorting; traversal itself is O(N + M).
      * Space: O(1) auxiliary space (excluding memory used by Timsort and the output list).

Learnings & Gotchas:
  - Checking `result[-1] != nums1[i]` prevents inserting adjacent duplicates into the output without needing a secondary set.
  - The Two-Pointer pattern avoids allocating dynamic hash table memory and is the exact pattern used when inputs are already sorted (or in external merge operations).
"""

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2)) #method 1: hash sets
    
        """
        method 2: two pointers
        nums1.sort()
        nums2.sort()

        i, j = 0, 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not result or result[-1] != nums1[i]:
                    result.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return result
        """