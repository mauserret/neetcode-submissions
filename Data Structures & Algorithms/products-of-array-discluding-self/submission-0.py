class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]

        suffix = [0] * len(nums)
        suffix[-1] = nums[-1]
        
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        ans = []
        prefix.insert(0, 1)
        suffix.append(1)

        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i+1])
        return ans
