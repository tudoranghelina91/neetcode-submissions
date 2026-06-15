"""
Use dictionary to count occurences of elements
Use frequency list where we group the numbers by occurences - e.g. 1x1, 2x2, 3x3
List can't have length greater than the number of elements - can't have more occurences than array length
After building freq we iterate in reverse order... last element represent most number of occurences
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        buckets = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for key, value in freq.items():
            buckets[value].append(key)

        result = []

        for i in range(len(buckets) - 1, -1, -1):
            while buckets[i]:
                item = buckets[i].pop()
                result.append(item)
                if len(result) == k:
                    return result
