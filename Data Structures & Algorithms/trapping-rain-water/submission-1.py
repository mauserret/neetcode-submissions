class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        prefix, suffix = [], []
        max_p, max_s = 0, 0

        for _ in range(len(height)):
            max_p = max(height[l], max_p)
            prefix.append(max_p)
            l+=1

            max_s = max(height[r], max_s)
            suffix.append(max_s)
            r-=1
        suffix = suffix[::-1]

        water = 0
        for i in range(len(height)):
            water += min(prefix[i], suffix[i]) - height[i]
        return water