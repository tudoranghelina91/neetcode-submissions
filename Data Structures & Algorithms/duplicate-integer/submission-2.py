"""
We use a dictionary (hashmap) to determine occurence
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occ = set()
        for num in nums:
            if num in occ:
                return True
            
            occ.add(num)
        
        return False

