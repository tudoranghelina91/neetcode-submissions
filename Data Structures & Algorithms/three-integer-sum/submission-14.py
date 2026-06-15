class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            # always skip duplicates from triplet first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s > 0:
                    k -= 1
                    continue
                
                if s < 0:
                    j += 1
                    continue
                

                result.append([nums[i], nums[j], nums[k]])

                # always ignore dupplicates from triplet last element
                while True:
                    j += 1
                    if j >= k or nums[j] != nums[j - 1]:
                        break
                    
        return result