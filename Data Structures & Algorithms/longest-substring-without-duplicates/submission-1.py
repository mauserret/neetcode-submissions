class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        chars = []
        #"zxyzxyz"
        for i in range(len(s)):
            while s[i] in chars:
                chars.remove(s[l])
                l += 1
            chars.append(s[i])
            longest = max(longest, i-l+1)
        return longest
