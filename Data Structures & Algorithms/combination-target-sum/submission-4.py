class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solution = []
        result = []
        
        def backtrack(i, crt_sum):
            if crt_sum == target:
                result.append(solution[:])
                return
            
            if crt_sum > target or i == len(nums):
                return

            backtrack(i + 1, crt_sum)

            solution.append(nums[i])

            backtrack(i, crt_sum + nums[i])
            solution.pop()

        backtrack(0, 0)

        return result