class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in hash:
                return [hash[remaining], i]
            
            hash[num] = i