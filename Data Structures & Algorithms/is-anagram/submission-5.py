class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for char in s:
            s_hash[char] = 1 + s_hash.get(char, 0)
        
        for char in t:
            t_hash[char] = 1 + t_hash.get(char, 0)

        return (s_hash == t_hash)