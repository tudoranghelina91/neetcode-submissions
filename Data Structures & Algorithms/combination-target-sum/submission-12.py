class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        res = []
        n = len(nums)
        def backtrack(crt_sum, i):
            if i == n or crt_sum > target:
                return
            
            if crt_sum == target:
                res.append(sol[:])
                return

            sol.append(nums[i])

            backtrack(crt_sum + nums[i], i)
            sol.pop()
            backtrack(crt_sum, i + 1)
        
        backtrack(0, 0)
        return res