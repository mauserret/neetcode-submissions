class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        ans = []
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        for _ in range(k):
            highest = max(hash.values())
            for key in hash.keys():
                if hash[key] == highest:
                    ans.append(key)
                    hash.pop(key)
                    break
        return ans

