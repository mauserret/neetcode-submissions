class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-4,-1,-1,0,1,2]
        
        ans = []
        nums.sort()

        for i in range(len(nums)-2):
            l = i+1
            if i > 0 and nums[i] == nums[i-1]:
                continue

            r = len(nums)-1
            while l < r:
                threeSum = nums[i]+nums[l]+nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1] :
                        l += 1
        return ans