class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
                continue
            r = m

        
        mini = l

        if mini == 0:
            l, r = 0, n - 1
        elif nums[0] <= target <= nums[mini - 1]:
            l, r = 0, mini - 1
        else:
            l, r = mini, n - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
                continue
            r = m - 1
        
        return -1
            