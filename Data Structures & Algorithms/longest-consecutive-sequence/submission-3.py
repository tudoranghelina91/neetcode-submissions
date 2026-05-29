class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res_set = set(nums)
        maxlen = 0

        for num in nums:
            if num - 1 not in res_set:
                length = 0
                while num + length in res_set:
                    length += 1

                maxlen = max(maxlen, length)

        return maxlen