"""
Use dictionary to count occurences of elements
Use frequency list where we group the numbers by occurences - e.g. 1x1, 2x2, 3x3
List can't have length greater than the number of elements - can't have more occurences than array length
After building freq we iterate in reverse order... last element is number of occurences
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res