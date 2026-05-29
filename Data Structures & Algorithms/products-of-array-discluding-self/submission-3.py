"""
left subarray stores product on left
right subarray stores product on right
we return a new array with the product of elements from both arrays
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        sufix = [1] * n

        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        for i in range(n - 2, -1, -1):
            sufix[i] = nums[i + 1] * sufix[i + 1]

        for i in range(n):
            nums[i] = prefix[i] * sufix[i]

        return nums