class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxSurface = 0

        while l < r:
            d = r - l
            surface = d * min(heights[l], heights[r])
            maxSurface = max(surface, maxSurface)

            if heights[l] < heights[r]:
                l += 1
                continue
            
            r -= 1

        return maxSurface