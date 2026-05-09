class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        n = len(nums)

        for i in range(n):
            l = i + 1
            r = n - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s > 0:
                    r -= 1
                    continue

                if s < 0:
                    l += 1
                    continue

                res.append([nums[i], nums[l], nums[r]])
                while(True):
                    l += 1
                    if l >= r or nums[l] != nums[l-1]:
                        break

        return res
        