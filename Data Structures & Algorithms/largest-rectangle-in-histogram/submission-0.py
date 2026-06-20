class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            start = i
            while stack and  stack[-1][1] > h :
                stack_i, stack_h = stack.pop()
                max_area = max(max_area, stack_h * (i - stack_i))
                start = stack_i
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
