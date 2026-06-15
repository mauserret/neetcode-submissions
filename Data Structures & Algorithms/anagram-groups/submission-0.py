class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in hash:
                hash[sorted_word].append(word)
            else: 
                hash[sorted_word] = [word]
        return list(hash.values())