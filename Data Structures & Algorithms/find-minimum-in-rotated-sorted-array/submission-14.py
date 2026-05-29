class Solution:
    """
    l < r
    set m to middle
    compare with rightmost value
    if greater, reduce from left
    otherwise reduce from right
    r = m
    """
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        return nums[l]