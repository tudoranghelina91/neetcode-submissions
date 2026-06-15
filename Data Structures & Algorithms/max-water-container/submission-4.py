class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        result = 0

        while l < r:
            h = min(heights[l], heights[r])
            d = r - l

            result = max(result, d * h)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return result