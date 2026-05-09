class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        # for num in nums:
        #     if target - num == hashmap[num]:
        #         return [hashmap[num], num]
        #     hashmap[target - num] = target - num

        for i, num in enumerate(nums):
            if target - num in hashmap:
                return [hashmap[target - num], i]
            
            hashmap[nums[i]] = i