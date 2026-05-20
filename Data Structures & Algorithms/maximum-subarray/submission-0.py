class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxabs = nums[0]
        maxsofar = nums[0]
        
        for num in nums[1:]:
            maxsofar = max(num, maxsofar + num)
            maxabs = max(maxabs, maxsofar)

        return maxabs