class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            print(m)
            if nums[m] > nums[-1]:
                l = m + 1
            elif nums[m] < nums[-1] and nums[m-1] < nums[-1]:
                r = m - 1
            else:
                return nums[m]