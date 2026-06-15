"""
Store index at target - num key in hashmap
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i in range(len(nums)):
            if target - nums[i] in complements:
                return [complements[target - nums[i]], i]
            
            complements[nums[i]] = i