class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solution = []
        result = []

        def backtrack(i, crtsum):
            if crtsum == target:
                result.append(solution[:])
                return

            if i == len(nums) or crtsum > target:
                return


            backtrack(i + 1, crtsum)
            solution.append(nums[i])
            backtrack(i, crtsum + nums[i])
            solution.pop()

        backtrack(0, 0)

        return result