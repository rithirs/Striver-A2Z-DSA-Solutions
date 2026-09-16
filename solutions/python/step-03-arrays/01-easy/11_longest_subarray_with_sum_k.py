"""
Problem: Striver Step 3.1 - Longest Subarray with Sum K (LC 325 Premium / GFG)
Approach:
  - Used a Prefix Sum + Hash Map pattern (`prefix_map`) to achieve an O(N) single-pass lookup.
  - Tracked running total in `current_sum` as we iterated through index `i`.
  - Case 1: If `current_sum == k`, the subarray starts from index 0, so length is `i + 1`.
  - Case 2: Checked if `(current_sum - k)` was recorded earlier in `prefix_map`.
    If present at `prev_idx`, the segment between `prev_idx + 1` and `i` sums to `k` (length = `i - prev_idx`).
  - Stored `prefix_map[current_sum] = i` ONLY if `current_sum` was not already recorded (earliest index maximizes length).

Complexity:
  - Time Complexity: O(N) — Single linear scan with O(1) hash map operations.
  - Space Complexity: O(N) — Storing up to N distinct prefix sums in the hash map.

Learnings & Gotchas:
  - Do NOT update `prefix_map[current_sum]` if it already exists; an earlier starting index yields a longer slice.
  - This hash map solution works for positives, zeros, and negative numbers.
Another way to solve this problem:

for start in range(len(nums)):
    current_sum = 0
    for end in range(start, len(nums)):
        current_sum += nums[end]  # add the next slice
        
        if current_sum == k:
            length = end - start + 1
            max_len = max(max_len, length)

print(max_len)

"""

def longestSubarrayWithSumK(nums: list[int], k: int) -> int:
    prefix_map = {}
    current_sum = 0
    max_len = 0

    for i in range(len(nums)):
        current_sum += nums[i]
        if current_sum == k:
            max_len = max(max_len, i + 1)

        needed = current_sum - k
        if needed in prefix_map:
            length = i - prefix_map[needed]
            max_len = max(max_len, length)

        if current_sum not in prefix_map:
            prefix_map[current_sum] = i

    return max_len