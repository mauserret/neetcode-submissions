class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        count_T, window = {}, {}

        for c in t:
            count_T[c] = 1 + count_T.get(c, 0)

        have, need = 0, len(count_T)

        res, res_len = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_T and window[c] == count_T[c]:
                have += 1

            while have == need:
                # Update result if the length is less
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                # Remove from the left of the window
                window[s[l]] -= 1
                if s[l] in count_T and window[s[l]] < count_T[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] 



        