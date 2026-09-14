from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[k] = nums[j]
                k+=1
        return k