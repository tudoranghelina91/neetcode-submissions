class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        m = (l + r) // 2
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                return min(res, nums[l])
            
            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
                continue
            
            r = m - 1

        return res