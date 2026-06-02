class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        
        # 1. find min
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
                continue
            
            r = m

        mini = l

        # 2. determine search window, before or after min
        if mini == 0:
            l, r = 0, n - 1
        elif nums[0] <= target <= nums[mini - 1]:
            l, r = 0, mini - 1
        else:
            l, r = mini, n - 1

        # 3. regular binary search
        while l <= r:
            m = (l + r) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m

        return -1