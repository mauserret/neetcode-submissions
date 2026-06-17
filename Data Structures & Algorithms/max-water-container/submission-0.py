class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            current_area = (r-l) * min(heights[l], heights[r])
            area = max(area, current_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return area