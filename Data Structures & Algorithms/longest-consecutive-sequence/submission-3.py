class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #[2,3,4,4,5,10,20]
        nums = sorted(nums)
        count = []
        longest = 0
        for i in range(len(nums)):
            if len(count) == 0:
                count.append(nums[i])
            elif nums[i] in count:
                continue
            elif count[-1] == nums[i]-1:
                count.append(nums[i])
            else:
                count = []
                count.append(nums[i])
            if len(count) > longest:
                longest = len(count)
        return longest
            
            
            
