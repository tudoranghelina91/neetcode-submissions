"""
left subarray stores product on left
right subarray stores product on right
we return a new array with the product of elements from both arrays
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * len(nums)
        suf = [1] * len(nums)

        for i in range(1, n):
            pref[i] = pref[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            nums[i] = pref[i] * suf[i]

        return nums