class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxabs = nums[0]
        crtmax = nums[0]
        
        for num in nums[1:]:
            crtmax = max(num, crtmax + num)
            maxabs = max(maxabs, crtmax)

        return maxabs