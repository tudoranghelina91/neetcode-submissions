class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find min
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        # determine search intervals
        mini = l

        if mini == 0:
            l, r = 0, len(nums) - 1
        elif nums[0] <= target <= nums[mini - 1]:
            l, r = 0, mini - 1
        else:
            l, r = mini, len(nums) - 1

        # binary search in min half
        while l <= r:
            m = (l + r) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        
        return -1