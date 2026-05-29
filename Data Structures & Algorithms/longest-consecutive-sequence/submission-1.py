class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res_set = set(nums)
        maxlen = 0

        for num in nums:
            length = 0
            if num - 1 in res_set:
                length = 0

            while num + length in res_set:
                length += 1

            maxlen = max(maxlen, length)

        return maxlen